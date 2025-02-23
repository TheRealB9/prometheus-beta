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
    
    # Simplified compression
    compressed = bytearray()
    i = 0
    
    while i < len(data):
        # Find potential match
        best_length = 0
        best_offset = 0
        
        # Look back for longest match
        search_start = max(0, i - 65535)  # 16-bit offset
        for j in range(search_start, i):
            match_length = 0
            
            # Check match continuation
            while (i + match_length < len(data) and 
                   j + match_length < i and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 255):
                match_length += 1
            
            # Update best match if needed
            if match_length > best_length:
                best_length = match_length
                best_offset = i - j
        
        # If a good match is found
        if best_length >= 4:
            # Token: 4 bits for match len, 4 bits for literal len
            match_bytes = min(best_length, 15)
            literal_bytes = 0  # No literals when we have a match
            token = (match_bytes << 4) | literal_bytes
            compressed.append(token)
            
            # Extra match length if needed
            if best_length >= 15:
                extra = best_length - 15
                compressed.append(extra)
            
            # Add 2-byte offset
            compressed.extend(best_offset.to_bytes(2, byteorder='little'))
            
            # Move forward
            i += best_length
        else:
            # No match: literal mode
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
    
    # Simplified LZ4 decoding
    while i < len(compressed_data):
        # Get the token
        token = compressed_data[i]
        i += 1
        
        # Extract match and literal lengths
        match_length = token >> 4
        literal_length = token & 0x0F
        
        # Handle extended literal length
        if literal_length == 15:
            while True:
                extra = compressed_data[i]
                i += 1
                literal_length += extra
                if extra != 255:
                    break
        
        # Copy literals
        if literal_length > 0:
            if i + literal_length > len(compressed_data):
                raise ValueError("Invalid compressed data: truncated literals")
            decompressed.extend(compressed_data[i:i+literal_length])
            i += literal_length
        
        # If at end of compressed data, stop
        if i >= len(compressed_data):
            break
        
        # Extract 2-byte offset
        if i + 1 >= len(compressed_data):
            raise ValueError("Invalid compressed data: incomplete offset")
        
        offset = int.from_bytes(compressed_data[i:i+2], byteorder='little')
        i += 2
        
        # Extended match length
        if match_length == 15:
            while True:
                extra = compressed_data[i]
                i += 1
                match_length += extra
                if extra != 255:
                    break
        
        # Reproduce match
        if match_length > 0:
            # Validate offset
            if offset > len(decompressed):
                raise ValueError("Invalid offset")
            
            # Repeat matched sequence
            start = len(decompressed) - offset
            for _ in range(match_length):
                # If this happens, likely an issue with decompression
                if start < 0 or start >= len(decompressed):
                    raise ValueError("Invalid match during decompression")
                
                decompressed.append(decompressed[start])
                start += 1
    
    return bytes(decompressed)