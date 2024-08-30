class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = str(bin(n)[2:])
        return ans.count('1')