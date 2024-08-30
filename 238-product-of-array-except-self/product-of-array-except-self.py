class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        ans = []
        for i in range(len(nums)):
                if nums[i] != 0:
                    total *= nums[i]
        if nums.count(0) == 0:
            for i in range(len(nums)):
                ans.append(total//nums[i])
            return ans
        else:
            if nums.count(0) == 1:
                for i in range(len(nums)):
                    if nums[i] != 0:
                        ans.append(0)
                    else:
                        ans.append(total)
            else:
                for i in range(len(nums)):
                    ans.append(0)
            return ans