def transform_array(input_array):
    """
    Transform an array of non-negative integers based on specific rules.
    
    Args:
        input_array (list): A list of non-negative integers.
    
    Returns:
        list: A new list where:
            - 0 remains 0
            - Non-zero elements are transformed to their square plus 1
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If any element is a negative number.
    """
    # Validate input is a list
    if not isinstance(input_array, list):
        raise TypeError("Input must be a list")
    
    # Create transformed array
    transformed = []
    
    # Transform each element
    for num in input_array:
        # Validate each element is a non-negative integer
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        
        if num < 0:
            raise ValueError("All elements must be non-negative")
        
        # Apply transformation rule
        if num == 0:
            transformed.append(0)
        else:
            transformed.append(num**2 + 1)
    
    return transformed