"""
Test suite for LZ4 compression implementation
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lz4_compression import lz4_compress, lz4_decompress

def test_compression_decompression_basic():
    """Test basic compression and decompression"""
    original = b"Hello, world! This is a test of LZ4 compression."
    compressed = lz4_compress(original)
    
    # Compressed data should be shorter or equal to original
    assert len(compressed) <= len(original)
    
    # Decompress and verify
    decompressed = lz4_decompress(compressed)
    assert decompressed == original

def test_compression_decompression_repeated_data():
    """Test compression with repeated data"""
    original = b"ABCABCABCABCABCABC" * 10
    compressed = lz4_compress(original)
    
    # Compressed data should be significantly shorter
    assert len(compressed) < len(original)
    
    # Decompress and verify
    decompressed = lz4_decompress(compressed)
    assert decompressed == original

def test_compression_decompression_string():
    """Test compression with string input"""
    original = "Hello, world! こんにちは"
    compressed = lz4_compress(original)
    
    # Decompress and verify
    decompressed = lz4_decompress(compressed)
    assert decompressed == original.encode('utf-8')

def test_empty_input_error():
    """Test error handling for empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lz4_compress(b"")
    
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        lz4_decompress(b"")

def test_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        lz4_compress(123)
    
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        lz4_decompress(123)

def test_minimal_compression():
    """Test compression of data with no repetition"""
    original = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    compressed = lz4_compress(original)
    
    # Decompress and verify
    decompressed = lz4_decompress(compressed)
    assert decompressed == original

def test_large_input():
    """Test compression of a larger input"""
    original = b"TEST DATA " * 1000
    compressed = lz4_compress(original)
    
    # Decompress and verify
    decompressed = lz4_decompress(compressed)
    assert decompressed == original