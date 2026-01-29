class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # First strategy - buy at lowest and sell whenever there is profit
        buy_price = prices[0]
        answer = 0
        for i in range(1, len(prices)):
            sell_price = prices[i]
            if sell_price > buy_price:
                answer += sell_price - buy_price
                buy_price = sell_price
            else:
                buy_price = sell_price
        return answer