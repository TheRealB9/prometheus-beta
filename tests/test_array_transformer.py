import pytest
from src.array_transformer import transform_array

def test_transform_array_basic_cases():
    # Test basic functionality
    assert transform_array([0, 1, 2, 3]) == [0, 2, 5, 10]
    assert transform_array([]) == []

def test_transform_array_zero_handling():
    # Test zero handling
    assert transform_array([0, 0, 0]) == [0, 0, 0]

def test_transform_array_error_handling():
    # Test type errors
    with pytest.raises(TypeError, match="Input must be a list"):
        transform_array(123)
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        transform_array([1, 2, '3'])
    
    with pytest.raises(ValueError, match="All elements must be non-negative"):
        transform_array([-1, 2, 3])

def test_transform_array_large_numbers():
    # Test large numbers
    result = transform_array([10, 20, 30])
    assert result == [101, 401, 901]

def test_transform_array_single_element():
    # Test single element cases
    assert transform_array([5]) == [26]
    assert transform_array([0]) == [0]