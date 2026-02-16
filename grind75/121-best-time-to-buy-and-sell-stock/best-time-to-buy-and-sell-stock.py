class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        best_buy_price = max(prices) + 1
        for buy, price_buy in enumerate(prices[:-1]):
            if price_buy >= best_buy_price:
                continue

            best_buy_price = price_buy
            best_sell_price = max(prices[buy:])
            profit = max(profit, best_sell_price - best_buy_price)
        return profit
        