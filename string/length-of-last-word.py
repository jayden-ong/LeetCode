class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        found_char = False
        curr_len = 0
        for i in range(len(s) - 1, -1, -1):
            if not found_char and s[i] != ' ':
                found_char = True
                curr_len += 1
            elif found_char and s[i] == ' ':
                return curr_len
            elif found_char and s[i] != ' ':
                curr_len += 1
        return curr_len