class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for i, j in intervals:
            if heap and i > heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, j)
        return len(heap)    