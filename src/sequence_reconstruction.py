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
    
    # Strict set comparison
    present_elements = set(arr)
    target_elements = set(original_sequence)
    
    if present_elements != target_elements:
        raise ValueError("Arrays must contain the same unique elements")
    
    # If identical, no operations needed
    if arr == original_sequence:
        return 0
    
    # Count inversions (hint to number of order-related operations)
    def count_inversions(sequence):
        inv_count = 0
        for i in range(len(sequence)):
            for j in range(i+1, len(sequence)):
                if sequence[i] > sequence[j]:
                    inv_count += 1
        return inv_count
    
    # Calculate complexity of reordering
    order_diff = count_inversions(arr) - count_inversions(original_sequence)
    
    # Absolute difference in length
    length_diff = abs(len(arr) - len(original_sequence))
    
    # Combine complexity metrics
    return max(order_diff, length_diff)