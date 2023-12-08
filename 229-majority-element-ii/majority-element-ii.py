class Solution:
    def majorityElement(self, nums):
        x = []
        temp = list(set(nums))
        for i in range(len(temp)):
            if nums.count(temp[i]) > len(nums)/3:
                x.append(temp[i])
        return x