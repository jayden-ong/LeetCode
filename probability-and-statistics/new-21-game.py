class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1
            
        answer = 0
        curr = 1
        dp = [1] * (n + 1)
        for i in range(1, n + 1):
            prob = curr / maxPts
            if 0 <= i - maxPts < k:
                curr -= dp[i - maxPts]

            if i < k:
                curr += prob
            else:
                answer += prob
            dp[i] = prob
        
        return answer
            
            