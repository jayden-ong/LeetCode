class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        num_prices = len(prices)
        answer = prices.copy()
        for i in range(num_prices):
            for j in range(i + 1, num_prices):
                if prices[j] <= prices[i]:
                    answer[i] = prices[i] - prices[j]
                    break
        return answer