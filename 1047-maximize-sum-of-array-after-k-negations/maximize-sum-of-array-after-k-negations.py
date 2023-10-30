class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        numbers = [0] * 201
        total_sum = 0
        max_abs = 0
        for n in nums:
            max_abs = max(max_abs, abs(n))
            numbers[100 + n] += 1
            total_sum += n
        if max_abs == 0:
            return 0
        while k > 0:
            k -= 1
            i = 100 - max_abs
            while numbers[i] == 0:
                i += 1
            numbers[i] -= 1
            numbers[200 - i] += 1
            total_sum -= 2 * (i - 100)
        return total_sum