class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hash and hash[val] != i:
                return [i, hash[val]]