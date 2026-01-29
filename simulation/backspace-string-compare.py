class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        curr_s = ""
        for i in range(len(s)):
            if s[i] == "#":
                if curr_s != "":
                    curr_s = curr_s[:-1]
            else:
                curr_s += s[i]
        
        curr_t = ""
        for i in range (len(t)):
            if t[i] == "#":
                if curr_t != "":
                    curr_t = curr_t[:-1]
            else:
                curr_t += t[i]
        return curr_s == curr_t