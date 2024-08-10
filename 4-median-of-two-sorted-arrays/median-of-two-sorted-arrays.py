class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        N = len(nums)
        if N%2==1:
            return nums[(N-1)//2]
        else:
            return (nums[round((N/2)-1)]+nums[round(N/2)])/2