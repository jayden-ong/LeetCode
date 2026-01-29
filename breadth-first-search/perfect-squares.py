class Solution:
    def numSquares(self, n: int) -> int:
        perfect_square_set = set()
        j = 0
        while j * j < n + 1:
            perfect_square_set.add(j * j)
            j += 1
        
        dp = []
        for i in range(n + 1):
            if i == 0:
                dp.append(0)
            elif i in perfect_square_set:
                dp.append(1)
            else:
                j = 1
                curr_best = float('inf')
                while j * j < i:
                    curr_best = min(curr_best, dp[i - j * j] + 1)
                    j += 1
                dp.append(curr_best)
        return dp[-1]