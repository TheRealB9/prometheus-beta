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
    
    # Shared elements between arrays
    common_elements = set(arr) & set(original_sequence)
    
    # Must share exact same set of unique elements
    if len(common_elements) != len(set(arr)) or len(common_elements) != len(set(original_sequence)):
        raise ValueError("Arrays must contain the same unique elements")
    
    # If sequences are identical, no operations needed
    if arr == original_sequence:
        return 0
    
    # Operations are either about removing/inserting or reordering
    # 1. Length difference
    length_diff = abs(len(arr) - len(original_sequence))
    
    # 2. Order changes: count mismatched positions
    order_changes = sum(x != y for x, y in zip(arr, original_sequence))
    
    # Resolve order changes for maximum confusion points
    return min(length_diff + 1, order_changes // 2)