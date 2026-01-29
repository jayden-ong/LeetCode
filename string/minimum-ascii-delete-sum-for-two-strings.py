class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # ord(char) gets ascii
        if len(s2) > len(s1):
            s1, s2 = s2, s1
        
        dp = [0] * (len(s2) + 1)
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] + ord(s2[j - 1])
        
        for i in range(1, len(s1) + 1):
            prev = dp[0]
            dp[0] += ord(s1[i - 1])

            for j in range(1, len(s2) + 1):
                temp = dp[j]
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j - 1] + ord(s2[j - 1]), temp + ord(s1[i - 1]))
                prev = temp
        return dp[len(s2)]