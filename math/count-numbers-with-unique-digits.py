class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # Store number of missing numbers
        # n = 3 -> 10 * 9 + 9 * 9
        dp = [1] * (n + 1)
        for i in range(1, n + 1):
            if i == 1:
                dp[i] = 10
            else:
                dp[i] = 9
                for j in range(2, i + 1):
                    dp[i] *= (11 - j)
                dp[i] += dp[i - 1]
        return dp[-1]