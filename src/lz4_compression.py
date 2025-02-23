"""
Simple LZ4-inspired Compression Algorithm

This is a basic implementation of a compression technique 
inspired by LZ4's principles of simple, fast compression.
"""

def lz4_compress(data):
    """
    Compress input data using a simplified compression method.
    
    Args:
        data (bytes or str): Input data to compress
    
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
        
        # Search back for longest match
        search_start = max(0, i - 255)  # Limit search window
        for j in range(search_start, i):
            match_length = 0
            
            # Extend match as long as possible
            while (i + match_length < len(data) and 
                   j + match_length < i and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 15):  # Limit match length
                match_length += 1
            
            # Update best match
            if match_length > best_length:
                best_length = match_length
                best_offset = i - j
        
        # Encode match or literal
        if best_length >= 4:
            # Encode match: first 4 bits are match length
            token = best_length
            compressed.append(token)
            compressed.append(best_offset)
            i += best_length
        else:
            # Literal byte
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def lz4_decompress(compressed_data):
    """
    Decompress data compressed with our method.
    
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
        # Get the token
        token = compressed_data[i]
        i += 1
        
        if token < 15:
            # Check if it's a match or literal
            if token == 0:
                # Literal byte
                decompressed.append(compressed_data[i-1])
            else:
                # Short match
                offset = compressed_data[i]
                i += 1
                
                # Reproduce matched sequence
                start = len(decompressed) - offset
                for _ in range(token):
                    # Ensure valid start index
                    if start < 0:
                        raise ValueError("Invalid offset in compressed data")
                    decompressed.append(decompressed[start])
                    start += 1
    
    return bytes(decompressed)