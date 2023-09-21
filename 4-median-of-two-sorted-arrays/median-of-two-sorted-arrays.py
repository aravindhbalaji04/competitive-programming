class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        N = round(len(nums))
        if N%2==1:
            median = nums[(N-1)//2]
            return median
        else:
            median = (nums[round((N/2)-1)]+nums[round(N/2)])/2
            return median
