class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        c = set(nums1) & set(nums2) 
        if c:
            return min(c)  
        else:
            return -1 