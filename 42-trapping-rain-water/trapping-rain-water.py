class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans, i, j, leftMax, rightMax = 0, 0, len(height)-1, height[0], height[len(height)-1]
        while i < j:
            if leftMax < rightMax:
                i += 1
                leftMax = max(leftMax, height[i])
                ans += leftMax - height[i]
            else:
                j -= 1
                rightMax = max(rightMax, height[j])
                ans += rightMax - height[j]
        return ans