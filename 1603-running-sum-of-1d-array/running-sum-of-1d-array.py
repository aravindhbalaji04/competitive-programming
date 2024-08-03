class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        val = 0
        ans = []
        for i in range(len(nums)):
            val += nums[i]
            ans.append(val)
        return ans