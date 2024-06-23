class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q, max_q, left, ans = deque(), deque(), -1, 0
        for i in range(len(nums)):
            while min_q and nums[min_q[-1]] > nums[i]:
                min_q.pop()
            min_q.append(i)
            while max_q and nums[max_q[-1]] < nums[i]:
                max_q.pop()
            max_q.append(i)
            if nums[max_q[0]] - nums[min_q[0]] > limit:
                left = min_q.popleft() if min_q[0] < max_q[0] else max_q.popleft()
            ans = max(i-left, ans)
        return ans