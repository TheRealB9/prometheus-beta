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
    
    # If input and target are identical
    if arr == original_sequence:
        return 0
    
    # Track common elements
    common_elements = list(filter(lambda x: x in original_sequence, arr))
    
    # If common elements don't match target sequence
    if common_elements != list(filter(lambda x: x in arr, original_sequence)):
        raise ValueError("Arrays must contain the same unique elements")
    
    # Calculate differences
    removals = len(arr) - len(common_elements)
    insertions = len(original_sequence) - len(common_elements)
    
    # Handle reordering
    order_changes = sum(x != y for x, y in zip(common_elements, original_sequence))
    
    return max(removals + insertions, order_changes // 2)