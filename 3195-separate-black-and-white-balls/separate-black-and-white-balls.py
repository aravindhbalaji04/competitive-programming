class Solution:
    def minimumSteps(self, s: str) -> int:
        t = s[::-1]
        ans = zero = 0
        for i in t:
            if i == '0':
                zero += 1
            else:
                ans += zero
        return ans