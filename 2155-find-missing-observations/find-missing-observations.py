class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_sum = mean * (len(rolls) + n)
        missing_sum = total_sum - sum(rolls)
        if missing_sum < n or missing_sum > 6 * n:
            return []
        res = [1] * n
        missing_sum -= n
        i = 0
        while missing_sum > 0:
            increment = min(5, missing_sum)
            res[i] += increment
            missing_sum -= increment
            i += 1
        return res