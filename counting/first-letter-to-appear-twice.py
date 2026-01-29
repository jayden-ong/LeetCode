class Solution:
    def repeatedCharacter(self, s: str) -> str:
        s_set = set()
        for char in s:
            if char in s_set:
                return char
            else:
                s_set.add(char)