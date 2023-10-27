class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = []
        y = list(set(nums))
        z = []
        for i in range(len(y)):
            if y[i] in nums:
                x.append(nums.count(y[i]))
                z.append(y[i])
        me = max(x)
        return y[x.index(me)]