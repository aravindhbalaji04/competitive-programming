class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        num = max(nums)
        for i in range(len(nums)):
            if nums[i]*2 > num and nums[i] != num:
                return -1
        return nums.index(num)