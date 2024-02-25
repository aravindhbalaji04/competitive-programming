from collections import Counter
import heapq

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:    
        max_value = 9999999999
        for i in range(len(changeIndices)):
            changeIndices[i] -= 1
        def can_mark(maximum_time):
            first_time_to_zero_num = [max_value for i in range(len(nums))]
            for i in range(len(changeIndices)):
                num_index = changeIndices[i]
                if nums[num_index] != 0:
                    first_time_to_zero_num[num_index] = min(first_time_to_zero_num[num_index], i)
            number_we_can_zero_at_time = {}
            for i in range(len(nums)):
                number_we_can_zero_at_time[first_time_to_zero_num[i]] = i
            min_heap = []
            time_available = 0
            for i in range(maximum_time - 1, -1, -1):
                if i in number_we_can_zero_at_time:
                    heapq.heappush(min_heap, nums[number_we_can_zero_at_time[i]])
                    if time_available > 0:
                        time_available -= 1
                    else:
                        time_available += 1
                        heapq.heappop(min_heap)
                else:
                    time_available += 1
            decrementing_total = (sum(nums) + len(nums)) - (sum(min_heap) + len(min_heap))
            zeroing_total = len(min_heap) * 2
            return decrementing_total + zeroing_total <= maximum_time
        left = 1
        right = len(changeIndices)
        while left < right:
            mid = left + (right - left) // 2
            if can_mark(mid):
                right = mid
            else:
                left = mid + 1
        if can_mark(left):
            return left
        return -1