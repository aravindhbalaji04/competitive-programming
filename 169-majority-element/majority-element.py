class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dick = {}
        n = len(nums)
        for i in nums:
            if i in dick:
                dick[i] += 1
            else:
                dick[i] = 1
            if dick[i] > n//2:
                return i