import pytest
from src.sequence_reconstruction import min_sequence_reconstruction

def test_basic_reconstruction():
    """Test a simple case of sequence reconstruction"""
    arr = [1, 2, 3, 4]
    original = [1, 2, 3, 4]
    assert min_sequence_reconstruction(arr, original) == 0

def test_single_different_order():
    """Test when elements are the same but in different order"""
    arr = [3, 1, 4, 2]
    original = [1, 2, 3, 4]
    assert min_sequence_reconstruction(arr, original) == 2

def test_some_elements_to_remove():
    """Test when some elements need to be removed"""
    arr = [1, 2, 3, 4, 5]
    original = [1, 2, 3]
    assert min_sequence_reconstruction(arr, original) == 2

def test_missing_elements():
    """Test when elements need to be inserted"""
    arr = [1, 2]
    original = [1, 2, 3, 4]
    assert min_sequence_reconstruction(arr, original) == 2

def test_complete_different_arrays():
    """Test when arrays are completely different"""
    arr = [1, 2, 3]
    original = [4, 5, 6]
    with pytest.raises(ValueError, match="must contain the same unique elements"):
        min_sequence_reconstruction(arr, original)

def test_none_input():
    """Test None input handling"""
    with pytest.raises(ValueError, match="Input arrays cannot be None"):
        min_sequence_reconstruction(None, [1, 2, 3])
    with pytest.raises(ValueError, match="Input arrays cannot be None"):
        min_sequence_reconstruction([1, 2, 3], None)

def test_empty_input():
    """Test empty input handling"""
    with pytest.raises(ValueError, match="Input arrays cannot be empty"):
        min_sequence_reconstruction([], [1, 2, 3])
    with pytest.raises(ValueError, match="Input arrays cannot be empty"):
        min_sequence_reconstruction([1, 2, 3], [])