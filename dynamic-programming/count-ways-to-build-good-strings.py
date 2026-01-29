class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Want to count how many ways you can form strings of all relevant lengths
        dp = defaultdict(int)
        answer = 0
        for i in range(high + 1):
            if zero == i:
                dp[i] += 1
            elif zero < i:
                dp[i] += dp[i - zero]
            
            if one == i:
                dp[i] += 1
            elif one < i:
                dp[i] += dp[i - one]
        
            if low <= i <= high:
                answer += dp[i]
        
        return answer % (pow(10, 9) + 7)
            
        
            