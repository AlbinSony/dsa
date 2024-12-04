class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mpp = {}
        for i, num in enumerate(nums):
            more = target - num
            if more in mpp:
                return [mpp[more], i]
            mpp[num] = i
        return [-1, -1]
