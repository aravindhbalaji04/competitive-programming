class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            if coins-costs[i] < 0:
                return i
            else:
                coins -= costs[i]
        return len(costs)