class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num_prices = len(prices)
        buy_price = prices[0]
        curr_profit = 0
        for i in range(1, num_prices):
            sell_price = prices[i]
            if sell_price > buy_price:
                curr_profit = max(curr_profit, sell_price - buy_price)
            else:
                buy_price = sell_price

        return curr_profit
            