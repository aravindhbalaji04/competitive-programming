class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        x = []
        for i in range(len(nums)):
            if nums[i]%2==0:
                x.append(nums[i])
        for i in range(len(nums)):
            if nums[i]%2==1:
                x.append(nums[i])
        return x