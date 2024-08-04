class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        x = []
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1 
            else:
                x.append(count)   
                count = 0
        x.append(count)
        return max(x)