class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == sorted(prices, reverse=True):
            return 0
        min_price, profit = prices[0], 0
        for i in prices[1:]:
            min_price = min(min_price, i)
            profit = max(profit, i-min_price)
        return profit