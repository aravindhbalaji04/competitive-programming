class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min,curr_max=1,1
        ans=nums[0]
        for i in nums:
            x = (i,i*curr_min,i*curr_max)
            curr_min,curr_max=min(x),max(x)

            ans = max(ans,curr_max)
        return ans
    