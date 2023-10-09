class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x = []
        for i in range(len(nums)):
            if target == nums[i]:
                x.append(i)
        if len(x) == 0:
            return [-1,-1]
        elif len(x) == 1:
            x.append(x[0])
            return x
        elif len(x) == 2:
            return x
        else:
            y = []
            y.append(x[0])
            y.append(x[len(x)-1])
            return y