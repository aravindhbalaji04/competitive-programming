class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mine, maxe, ans = arrays[0][0], arrays[0][-1], 0
        for i in range(1, len(arrays)):
            ans = max(ans, abs(arrays[i][-1] - mine))
            ans = max(ans, abs(maxe - arrays[i][0]))
            mine = min(mine, arrays[i][0])
            maxe = max(maxe, arrays[i][-1])        
        return ans