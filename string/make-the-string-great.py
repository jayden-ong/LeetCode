class Solution:
    def makeGood(self, s: str) -> str:
        #abcCBA -> abBA
        i = 0
        curr_len = len(s)
        while i < curr_len - 1:
            if (s[i].upper() == s[i + 1] and s[i + 1].lower() == s[i]) or (s[i].lower() == s[i + 1] and s[i + 1].upper() == s[i]):
                if i + 2 >= curr_len:
                    s = s[:i]
                else:
                    s = s[:i] + s[i + 2:]
                if i > 0:
                    i -= 1
                curr_len -= 2
            else:
                i += 1
        return s