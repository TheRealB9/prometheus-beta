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
    
    # If sequence contains all unique elements from input
    present_elements = set(arr)
    target_elements = set(original_sequence)
    
    # Compute insertions and deletions
    insertions = len(target_elements - present_elements)
    deletions = len(present_elements - target_elements)
    
    # If all elements are shared, calculate order changes
    if len(present_elements) == len(target_elements):
        # Count mismatched positions
        order_changes = sum(x != y for x, y in zip(arr, original_sequence)) // 2
        
        # Prefer minimum between order changes and length difference
        return min(abs(len(arr) - len(original_sequence)) + insertions + deletions, 
                   order_changes)
    
    return insertions + deletions