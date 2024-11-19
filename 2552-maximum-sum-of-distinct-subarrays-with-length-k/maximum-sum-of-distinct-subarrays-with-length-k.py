class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = total = i = j = 0
        dick = {}
        while j < len(nums):
            a = nums[j]
            b = dick.get(a, -1)
            while i <= b or j-i+1 > k:
                total -= nums[i]
                i += 1
            dick[a] = j
            total += nums[j]
            if j-i+1 == k:
                ans = max(ans, total)
            j += 1
        return ans