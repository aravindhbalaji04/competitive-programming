class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        inf = float('inf')
        G = {}
        for _from, _to, price in flights:
            G.setdefault(_from, []).append((_to, price))
        vertex = [1 for i in range(n)]
        prices = [(inf, 0) for i in vertex]
        prices[src] = (0, 0)
        h = [(0, src, 0)]
        heapq.heapify(h)
        while h:
            price, v, step = heapq.heappop(h)
            vertex[v] = 0
            if v == dst:
                break
            if v in G:
                next = step + 1
                for u, p in G[v]:
                    if step <= k:
                        r = price + p
                        if vertex[u] and prices[u][0] > r:
                            prices[u] = (r, next)
                            heapq.heappush(h, (r, u, next))
                        elif prices[u][1] > step:
                            heapq.heappush(h, (r, u, next))
        return prices[dst][0] if prices[dst][0] < inf else -1