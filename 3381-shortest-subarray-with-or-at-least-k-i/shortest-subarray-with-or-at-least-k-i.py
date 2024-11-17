class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            OR = 0
            for j in range(i, n):
                OR = OR | nums[j]
                if OR >= k:
                    ans = min(ans, (j - i) + 1)
        if ans == float('inf'):
            return -1
        else:
            return ans