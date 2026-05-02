class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        else:
            max_prices = 0
            min_buy = prices[0]
            for sale in prices:
                max_prices = max(max_prices, sale - min_buy)
                min_buy = min(min_buy, sale)
            return max_prices
        