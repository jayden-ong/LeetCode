class Solution:
    def minimizedStringLength(self, s: str) -> int:
        char_set = set()
        for char in s:
            char_set.add(char)
        return len(char_set)