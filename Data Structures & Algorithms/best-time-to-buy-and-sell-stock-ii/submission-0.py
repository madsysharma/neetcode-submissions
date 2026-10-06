class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        n = len(prices)
        max_profit = 0
        peak, valley = 0, 0
        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = i
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = i
            max_profit += prices[peak] - prices[valley]
        return max_profit