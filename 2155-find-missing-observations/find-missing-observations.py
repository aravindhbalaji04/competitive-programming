class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean*(len(rolls)+n)
        miss = total-sum(rolls)
        if miss < n or miss > 6*n:
            return []
        res = [1]*n
        miss -= n
        i = 0
        while miss:
            j = min(5, miss)
            res[i] += j
            miss -= j
            i += 1
        return res