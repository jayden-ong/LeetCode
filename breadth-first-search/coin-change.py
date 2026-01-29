class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_set = set(coins)
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            if i in coins_set:
                dp[i] = 1
            else:
                curr_answer = float('inf')
                for coin in coins_set:
                    if i - coin >= 0 and dp[i - coin] != -1:
                        curr_answer = min(curr_answer, dp[i - coin] + 1)
                if curr_answer != float('inf'):
                    dp[i] = curr_answer
        return dp[-1]
