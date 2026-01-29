class Solution:
    def scoreOfString(self, s: str) -> int:
        length_s = len(s)
        answer = 0
        for i in range(1, length_s):
            answer += abs(ord(s[i]) - ord(s[i - 1]))
        return answer