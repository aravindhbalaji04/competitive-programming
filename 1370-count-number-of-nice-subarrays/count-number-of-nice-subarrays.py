class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        binary_nums = [1 if num % 2 == 1 else 0 for num in nums]
        prefix_sum_count = {0:1}
        current_sum = 0
        result = 0
        for num in binary_nums:
            current_sum += num
            if current_sum - k in prefix_sum_count:
                result += prefix_sum_count[current_sum - k]
            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1
        return result