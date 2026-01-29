class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)
        for i in range(0, haystack_length):
            if i + needle_length <= haystack_length and haystack[i:i + needle_length] == needle:
                return i
        return -1