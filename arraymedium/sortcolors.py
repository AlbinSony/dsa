class Solution:
    def sortColors(self, nums):
        n = len(nums)
        l, m, h = 0, 0, n - 1
        
        while m <= h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:  # nums[m] == 2
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
