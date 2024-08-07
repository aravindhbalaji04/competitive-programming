class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        common = set()
        for num in nums2:
            if num in s:
                common.add(num)
        return common
