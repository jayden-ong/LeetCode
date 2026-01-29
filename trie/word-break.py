class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        dp = []
        dp.append(True)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in word_set and dp[j]:
                    dp.append(True)
                    break
            if len(dp) == i:
                dp.append(False)
        return dp[-1]