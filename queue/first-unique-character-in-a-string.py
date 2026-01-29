class Solution:
    def firstUniqChar(self, s: str) -> int:
        alpha_dict = {}
        
        num_chars = 0
        for char in s:
            alpha_dict[char] = alpha_dict.get(char, 0) + 1
            num_chars += 1

        for i in range(num_chars):
            if alpha_dict[s[i]] == 1:
                return i
        return -1