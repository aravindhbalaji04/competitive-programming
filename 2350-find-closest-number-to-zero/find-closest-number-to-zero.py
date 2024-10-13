class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = abs(nums[0])
        for i in range(1, len(nums)):
            ans = min(ans, abs(nums[i]))
        if ans*-1 in nums and ans not in nums:
            return ans*-1
        return ans