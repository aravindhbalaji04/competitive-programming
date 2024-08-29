class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, i, j, ma, length = 0, 0, len(height)-1, max(height), len(height)
        while i < j:    
            if ans >= ma*length:
                break
            ans = max(ans, min(height[i],height[j])*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans