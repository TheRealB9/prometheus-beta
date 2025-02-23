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
    
    # Check containment
    if not set(arr).issuperset(set(original_sequence)):
        raise ValueError("Arrays must contain the same unique elements")
    
    # Calculate different aspects of transformation
    length_diff = abs(len(arr) - len(original_sequence))
    order_changes = len([1 for x, y in zip(arr, original_sequence) if x != y])
    
    # Different scenarios require different strategy
    if len(arr) > len(original_sequence):
        # Removal scenario
        return min(length_diff, order_changes // 2)
    elif len(arr) < len(original_sequence):
        # Insertion scenario
        return min(length_diff, order_changes // 2)
    else:
        # Reordering scenario
        return order_changes // 2