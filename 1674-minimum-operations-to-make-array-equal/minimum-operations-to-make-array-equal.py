class Solution:
    def minOperations(self, n: int) -> int:
        return round((n**2-1)/4)