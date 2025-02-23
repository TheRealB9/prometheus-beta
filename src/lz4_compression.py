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
        # Look for repeated sequences
        best_length = 0
        best_offset = 0
        
        # Search back for best match
        search_start = max(0, i - 65535)  # 16-bit offset
        for j in range(search_start, i):
            match_length = 0
            
            # Verify match continuation 
            while (i + match_length < len(data) and 
                   j + match_length < i and
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 255):
                match_length += 1
            
            # Update best match
            if match_length > best_length:
                best_length = match_length
                best_offset = i - j
        
        # Encode the match or literal
        if best_length >= 4:
            # Token: first literal (0), then match
            # Check if token is single byte
            if best_offset <= 255 and best_length <= 15:
                # Short form: token packed with lengths
                token = best_length 
                compressed.append(token)
                compressed.append(best_offset)
                i += best_length
            else:
                # Longer form 
                token = 15  # Maximum single-byte length 
                compressed.append(token)
                
                # Extra match length
                extra_match = best_length - 15
                compressed.append(extra_match)
                
                # 2-byte offset
                compressed.extend(best_offset.to_bytes(2, byteorder='little'))
                
                i += best_length
        else:
            # Literal byte
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
        # Get the token/length
        token = compressed_data[i]
        i += 1
        
        if token < 15:
            # Literal or short match
            if token < 15:
                # Add single byte literal or do match
                if token == 0:
                    # Literal
                    decompressed.append(compressed_data[i-1])
                else:
                    # Short match
                    offset = compressed_data[i]
                    i += 1
                    
                    # Reproduce the matched sequence
                    start = len(decompressed) - offset
                    for _ in range(token):
                        decompressed.append(decompressed[start])
                        start += 1
        else:
            # Long form
            match_length = token
            
            # Check for extra match length
            if match_length == 15:
                while True:
                    extra = compressed_data[i]
                    i += 1
                    match_length += extra
                    if extra != 255:
                        break
            
            # Extract 2-byte offset
            offset = int.from_bytes(compressed_data[i:i+2], byteorder='little')
            i += 2
            
            # Reproduce the matched sequence
            start = len(decompressed) - offset
            for _ in range(match_length):
                decompressed.append(decompressed[start])
                start += 1
    
    return bytes(decompressed)