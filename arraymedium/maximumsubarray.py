class Solution:
    def maxSubArray(self, nums):
        current_sum = 0
        max_sum = float('-inf')  # Equivalent to INT_MIN in C++
        
        for num in nums:
            current_sum += num
            max_sum = max(current_sum, max_sum)
            if current_sum < 0:
                current_sum = 0  # Reset sum if it becomes negative
        
        return max_sum
