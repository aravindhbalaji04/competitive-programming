class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = temp = 0
        target = max(nums)
        for i in nums:
            if i == target:
                temp += 1
                ans = max(ans, temp)
            else:
                temp = 0
        return ans