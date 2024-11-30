def longestSubarrayWithSumK(arr, k):
    preSumMap = {}  # Dictionary to store prefix sums and their first occurrence index
    sum = 0  # Cumulative sum
    maxLen = 0  # Length of the longest subarray with sum k
    
    for i in range(len(arr)):
        sum += arr[i]  # Update the cumulative sum
        
        # Case 1: If the cumulative sum equals k, the subarray starts from index 0
        if sum == k:
            maxLen = max(maxLen, i + 1)
        
        # Case 2: Check if the required prefix sum exists in the map
        rem = sum - k
        if rem in preSumMap:
            length = i - preSumMap[rem]  # Length of the subarray
            maxLen = max(maxLen, length)  # Update the max length
        
        # Case 3: Store the current prefix sum in the map if it's not already present
        if sum not in preSumMap:
            preSumMap[sum] = i
    
    return maxLen
