class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            curr = i ** x
            # No point in exploring greater bases as this answer is just equal to previous answer
            if curr > n:
                break
            # We cannot use i ** x for anything smaller than curr, since it is too large
            for j in range(n, curr - 1, -1):
                dp[j] = (dp[j] + dp[j - curr]) % MOD
        return dp[n]