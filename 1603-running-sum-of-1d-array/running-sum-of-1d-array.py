class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = []
        value = 0
        for i in range(len(nums)):
            value += nums[i]
            x.append(value)
        return x