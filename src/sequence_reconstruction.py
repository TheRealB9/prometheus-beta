def min_sequence_reconstruction(arr, original_sequence):
    """
    Determine the minimum number of insertions and removals required to 
    reconstruct an original sequence from a given array.
    
    Args:
        arr (list): The input array to be transformed
        original_sequence (list): The target original sequence
    
    Returns:
        int: Minimum number of insertions and removals needed
    
    Raises:
        ValueError: If input arrays are empty or None
    """
    # Validate inputs
    if arr is None or original_sequence is None:
        raise ValueError("Input arrays cannot be None")
    
    if not arr or not original_sequence:
        raise ValueError("Input arrays cannot be empty")
    
    # Special case for identical arrays
    if arr == original_sequence:
        return 0
    
    # Convert lists to sets for checking unique elements
    arr_set = set(arr)
    orig_set = set(original_sequence)
    
    # Allow different orders, but same unique set of elements
    if arr_set != orig_set:
        raise ValueError("Arrays must contain the same unique elements")
    
    # Number of operations is the difference in length between arrays
    return abs(len(arr) - len(original_sequence)) + abs(len(set(arr) - set(original_sequence)))