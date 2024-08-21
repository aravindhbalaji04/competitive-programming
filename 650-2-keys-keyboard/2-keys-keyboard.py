class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        else:
            for i in range(n-1,1,-1):
                if n % i == 0:
                    return round(Solution().minSteps(i) + n/i)
        return n