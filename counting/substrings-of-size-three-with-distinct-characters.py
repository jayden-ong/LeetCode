class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        length_s = len(s)
        if length_s < 3:
            return 0
        
        answer = 0
        for i in range(2, length_s):
            if s[i] == s[i - 1] or s[i - 1] == s[i - 2] or s[i] == s[i - 2]:
                continue
            else:
                answer += 1
        return answer