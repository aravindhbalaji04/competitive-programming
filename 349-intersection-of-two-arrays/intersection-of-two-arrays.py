class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sub = []
        for i in nums1:
            if i in nums2:
                if i not in sub:
                    sub.append(i)
        return sub