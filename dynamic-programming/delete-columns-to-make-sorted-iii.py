class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        dp = [1] * len(strs[0])
        for i in range(1, len(strs[0])):
            for j in range(i):
                valid = True
                for string in strs:
                    if string[j] > string[i]:
                        valid = False
                        break
                
                if valid:
                    dp[i] = max(dp[i], dp[j] + 1)

        return len(strs[0]) - max(dp)