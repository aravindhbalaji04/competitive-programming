class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minc, maxc, ans = arrays[0][0], arrays[0][-1], 0
        for i in range(1, len(arrays)):
            ans = max(ans, abs(arrays[i][-1] - minc))
            ans = max(ans, abs(maxc - arrays[i][0]))
            minc = min(minc, arrays[i][0])
            maxc = max(maxc, arrays[i][-1])        
        return ans