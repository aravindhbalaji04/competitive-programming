class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        x = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                x += 1
        if x > 0:
            best, total = 0, 0
            for i in range(len(nums)):
                total = max(nums[i],total+nums[i])
                best = max(best,total)
            return best
        else:
            best, total = nums[0], nums[0]
            for i in range(len(nums)):
                total = max(nums[i],total+nums[i])
                best = max(best,total)
            return best