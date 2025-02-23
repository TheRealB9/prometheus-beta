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
    
    # Check if both have same unique set of elements
    if set(arr) != set(original_sequence):
        raise ValueError("Arrays must contain the same unique elements")
    
    # Count inversions to understand reordering complexity
    def count_inversions(sequence, target):
        inversions = 0
        # Track indices of target sequence's elements in current sequence
        indices = [sequence.index(x) for x in target]
        
        for i in range(len(indices)):
            for j in range(i+1, len(indices)):
                if indices[i] > indices[j]:
                    inversions += 1
        return inversions
    
    # Compute complexity
    order_changes = count_inversions(arr, original_sequence)
    length_diff = abs(len(arr) - len(original_sequence))
    
    # Strategy: balance between reordering and length changes
    return max(order_changes // 2, length_diff)