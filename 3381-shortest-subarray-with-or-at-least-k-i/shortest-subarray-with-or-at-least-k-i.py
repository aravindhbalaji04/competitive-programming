class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        orarr, lenarr = [], []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                temp = nums[i]
                op = 1
                for l in range(i+1, j+1):
                    op += 1
                    temp |= nums[l]
                if temp >= k:
                    orarr.append(temp)
                    lenarr.append(op)
        ans = len(nums)
        status = 0
        for i in range(len(orarr)):
            status = 1
            ans = min(ans, lenarr[i])
        if status:
            return ans
        return -1