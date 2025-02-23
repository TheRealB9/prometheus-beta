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
    
    # Convert lists to sets for efficient membership checking
    arr_set = set(arr)
    orig_set = set(original_sequence)
    
    # Check if elements in arr match elements in original sequence
    if arr_set != orig_set:
        raise ValueError("Arrays must contain the same unique elements")
    
    # Calculate insertions and removals using the Longest Common Subsequence (LCS) concept
    def lcs_length(seq1, seq2):
        m, n = len(seq1), len(seq2)
        # Initialize DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if seq1[i-1] == seq2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    # Find length of longest common subsequence
    lcs = lcs_length(arr, original_sequence)
    
    # Minimum operations = total length - LCS length
    total_ops = (len(arr) - lcs) + (len(original_sequence) - lcs)
    
    return total_ops