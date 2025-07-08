class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        min_buy = prices[0]
        for price in prices:
            profit = price - min_buy
            if profit > max_profit:
                max_profit = profit
            if price < min_buy:
                min_buy = price

        return max_profit