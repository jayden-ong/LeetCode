class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        dp[0] = 0
        for i in range(1, days[-1] + 1):
            if i in days:
                possibilities = []
                # one day
                possibilities.append(costs[0] + dp[i - 1])
                # seven days
                if i < 7:
                    possibilities.append(costs[1])
                else:
                    possibilities.append(costs[1] + dp[i - 7])
                # thirty days
                if i < 30:
                    possibilities.append(costs[2])
                else:
                    possibilities.append(costs[2] + dp[i - 30])
                
                dp[i] = min(possibilities)
            else:
                dp[i] = dp[i - 1]
        return dp[days[-1]]