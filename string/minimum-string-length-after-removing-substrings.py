class Solution:
    def minLength(self, s: str) -> int:
        answer = len(s)
        i = 0
        while i < len(s) - 1:
            if s[i] + s[i + 1] == "AB" or s[i] + s[i + 1] == "CD":
                s = s[:i] + s[i + 2:]
                if i > 0:
                    i -= 1
                answer -= 2
            else:
                i += 1
        return answer