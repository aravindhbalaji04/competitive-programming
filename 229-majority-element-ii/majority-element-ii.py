class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        y = []
        z = []
        for i in range(len(nums)):
            a = nums.count(nums[i])
            if a > len(nums)/3:
                y.append(nums[i])
        for i in range(len(y)):
            if y[i] not in z:
                z.append(y[i])
        return z