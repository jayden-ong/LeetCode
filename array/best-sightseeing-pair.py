class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Keep track of the maximum element for everything after, taking distance into account
        dp = [0] * len(values)
        curr_best = values[-1] - 1
        for i in range(len(values) - 2, -1, -1):
            dp[i] = curr_best
            curr_best = max(curr_best - 1, values[i] - 1)
        
        answer = 0
        for i in range(len(values) - 1):
            answer = max(answer, values[i] + dp[i])
        return answer
