class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        dp = []
        curr = 0
        for word in words:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                curr += 1
            dp.append(curr)
        
        answer = []
        for l, r in queries:
            if l == 0:
                answer.append(dp[r])
            else:
                answer.append(dp[r] - dp[l - 1])
        return answer