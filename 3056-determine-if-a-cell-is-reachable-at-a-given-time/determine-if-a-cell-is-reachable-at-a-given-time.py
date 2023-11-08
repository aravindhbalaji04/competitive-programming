class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        xDistance = abs(sx - fx)
        yDistance = abs(sy - fy)
        minDist = min(xDistance, yDistance) + abs(yDistance - xDistance)
        if minDist == 0:
            return t != 1
        return t >= minDist
        