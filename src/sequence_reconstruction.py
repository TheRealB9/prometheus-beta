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
    
    # Calculate unique elements in both arrays
    arr_set = set(arr)
    orig_set = set(original_sequence)
    
    # Raise error if unique elements are different
    if arr_set != orig_set:
        raise ValueError("Arrays must contain the same unique elements")
    
    # Special case when arrays are already matched
    if arr == original_sequence:
        return 0
    
    # Calculate minimal operations needed
    # Removals: elements in arr not in the original sequence order
    # Insertions: elements in original sequence not in current order
    # Example: arr=[3,1,4,2], orig=[1,2,3,4]
    # We want to minimize changes to match order and length
    
    # Calculate number of operations (removals or insertions)
    length_diff = abs(len(arr) - len(original_sequence))
    order_changes = sum(1 for x, y in zip(arr, original_sequence) if x != y)
    
    return max(length_diff, order_changes)