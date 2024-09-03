import sys
sys.set_int_max_str_digits(10**9)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n <= 4:
            return 0
        ans, count = n, 0
        for i in range(1, n):
            ans *= i
        ans = str(ans)
        for i in range(len(ans)-1, -1, -1):
            if ans[i] == '0':
                count += 1
            else:
                return count