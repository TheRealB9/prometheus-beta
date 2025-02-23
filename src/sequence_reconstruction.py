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
    
    # Helper function to find the longest common subsequence
    def lcs(x, y):
        m, n = len(x), len(y)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if x[i-1] == y[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    # Check if all elements are the same (sets match)
    if set(arr) != set(original_sequence):
        raise ValueError("Arrays must contain the same unique elements")
    
    # If arrays are identical, no operations needed
    if arr == original_sequence:
        return 0
    
    # Calculate minimum operations using length difference 
    # and positions that differ
    lcs_length = lcs(arr, original_sequence)
    return len(arr) + len(original_sequence) - 2 * lcs_length