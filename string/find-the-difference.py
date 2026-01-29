class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        
        for char in t:
            if s_dict.get(char, -1) == -1 or s_dict[char] == 0:
                return char
            else:
                s_dict[char] -= 1
