class Solution:
    def majorityElement(self, nums):
        x = []
        for i in range(len(nums)):
            if nums.count(nums[i]) > len(nums)/3:
                x.append(nums[i])
        return list(set(x))