"""
LZ4 Compression Algorithm Implementation

This module provides a basic implementation of the LZ4 compression algorithm.
Note: This is a simplified version and not a full production-ready implementation.
"""

def lz4_compress(data):
    """
    Compress input data using a simplified LZ4 compression algorithm.
    
    Args:
        data (bytes or str): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input is empty
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert to bytes if input is a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Simplified LZ4-like compression
    compressed = bytearray()
    i = 0
    
    while i < len(data):
        # Look for repeated sequences
        best_length = 0
        best_offset = 0
        
        # Search back for longest matching sequence
        search_start = max(0, i - 65535)  # LZ4 uses a 16-bit offset
        for j in range(search_start, i):
            match_length = 0
            
            # Check how long the match continues
            while (i + match_length < len(data) and 
                   j + match_length < i and
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 255):  # Limit match length
                match_length += 1
            
            # Update best match if this is longer
            if match_length > best_length:
                best_length = match_length
                best_offset = i - j
        
        # Encode the match or literal
        if best_length >= 4:  # Minimum match length
            # Token: first 4 bits are match length, last 4 are literal length
            token = min(best_length, 15)
            compressed.append(token)
            
            # Add additional match length if needed
            if best_length >= 15:
                extra_length = best_length - 15
                compressed.append(extra_length)
            
            # Add offset as 2 bytes (little-endian)
            compressed.extend(best_offset.to_bytes(2, byteorder='little'))
            
            i += best_length
        else:
            # Encode literal byte
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def lz4_decompress(compressed_data):
    """
    Decompress LZ4-compressed data.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or compressed data is invalid
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Decompress
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Get the token (first byte)
        token = compressed_data[i]
        i += 1
        
        # Extract match and literal lengths
        match_length = token >> 4  # First 4 bits
        literal_length = token & 0x0F  # Last 4 bits
        
        # Add extra literal length bytes if needed
        if literal_length == 15:
            while True:
                extra = compressed_data[i]
                i += 1
                literal_length += extra
                if extra != 255:
                    break
        
        # Copy literals
        if literal_length > 0:
            decompressed.extend(compressed_data[i:i+literal_length])
            i += literal_length
        
        # If at end of data, stop
        if i >= len(compressed_data):
            break
        
        # Extract offset
        offset = int.from_bytes(compressed_data[i:i+2], byteorder='little')
        i += 2
        
        # Get match length
        base_match_length = token >> 4
        match_length = base_match_length
        if base_match_length == 15:
            while True:
                extra = compressed_data[i]
                i += 1
                match_length += extra
                if extra != 255:
                    break
        
        # Reproduce the matched sequence
        start = len(decompressed) - offset
        for _ in range(match_length):
            decompressed.append(decompressed[start])
            start += 1
    
    return bytes(decompressed)