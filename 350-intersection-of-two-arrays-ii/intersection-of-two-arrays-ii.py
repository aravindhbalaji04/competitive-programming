class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            mine = nums2
            maxe = nums1
        else:
            mine = nums1
            maxe = nums2
        ans = []
        for i in range(len(mine)):
            if mine[i] in maxe:
                ans.append(mine[i])
                maxe.remove(mine[i])
        return ans