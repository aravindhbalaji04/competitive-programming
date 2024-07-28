class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = [[] for _ in range(n+1)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        dist1 = [inf] * (n+1)
        dist2 = [inf] * (n+1)
        freq = [0] * (n+1)
        minHeap = []
        heappush(minHeap, (0,1))
        dist1[1] = 0
        while minHeap:
            timeTaken, node = heappop(minHeap)
            freq[node] += 1
            if freq[node] == 2 and node == n:
                return timeTaken
            if (timeTaken // change) % 2:
                timeTaken = change * (timeTaken // change + 1) + time
            else:
                timeTaken += time
            for neighbor in adj[node]:
                if freq[neighbor] == 2:
                    continue
                if dist1[neighbor] > timeTaken:
                    dist2[neighbor] = dist1[neighbor]
                    dist1[neighbor] = timeTaken
                    heappush(minHeap, (timeTaken, neighbor))
                elif dist2[neighbor] > timeTaken and dist1[neighbor] != timeTaken:
                    dist2[neighbor] = timeTaken
                    heappush(minHeap, (timeTaken, neighbor))
        return 0