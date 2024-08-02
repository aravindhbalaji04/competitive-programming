class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 2
        if len(nums) == 1:
            return 1
        else:
            while j < len(nums):
                if nums[j] != nums[i]:
                    nums[i+2] = nums[j]
                    i += 1
                j += 1
        return i+2