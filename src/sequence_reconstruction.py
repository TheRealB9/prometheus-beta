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
        ValueError: If input arrays are empty or None or have different elements
    """
    # Validate inputs
    if arr is None or original_sequence is None:
        raise ValueError("Input arrays cannot be None")
    
    if not arr or not original_sequence:
        raise ValueError("Input arrays cannot be empty")
    
    # Ensure exact same unique elements
    if set(arr) != set(original_sequence):
        raise ValueError("Arrays must contain the same unique elements")
    
    # If input and target are identical
    if arr == original_sequence:
        return 0
    
    # Compute positions that differ
    def compute_order_changes(source, target):
        # Create a map of element to its index in target
        target_index = {val: idx for idx, val in enumerate(target)}
        source_indices = [target_index[val] for val in source]
        
        # Count inversions
        inv_count = 0
        for i in range(len(source_indices)):
            for j in range(i+1, len(source_indices)):
                if source_indices[i] > source_indices[j]:
                    inv_count += 1
        return inv_count
    
    # Decide between length-based or position-based operations
    order_changes = compute_order_changes(arr, original_sequence)
    length_diff = abs(len(arr) - len(original_sequence))
    
    # Balance between reordering and length changes
    return max(order_changes // 2, length_diff)