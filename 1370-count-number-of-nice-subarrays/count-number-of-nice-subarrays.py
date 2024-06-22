class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count_map = defaultdict(int)
        count_map[0] = 1
        odd_count = 0
        ans = 0
        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            if odd_count >= k:
                ans += count_map[odd_count - k]
            count_map[odd_count] += 1
        return ans