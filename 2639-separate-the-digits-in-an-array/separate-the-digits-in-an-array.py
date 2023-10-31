class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        x = []
        for i in range(len(nums)):
            if len(str(nums[i])) > 1:
                for j in range(len(str(nums[i]))):
                    x.append(int(str(nums[i])[j]))
            else:
                x.append(nums[i])
        return x