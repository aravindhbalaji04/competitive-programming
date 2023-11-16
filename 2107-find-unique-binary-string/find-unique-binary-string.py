class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        size = len(nums)
        nums.sort()
        pointer = 0
        for i in range(size):
            decimal_value = int(nums[i], 2)
            if decimal_value == pointer:
                pointer += 1
            else:
                return format(pointer, f'0{size}b')
        return format(pointer, f'0{size}b')