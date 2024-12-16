class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k > 0:
            k -= 1
            i = nums.index(min(nums))
            nums[i] *= multiplier
        return nums