class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Only need to check lengths that are a factor of the length of the string
        string_length = len(s)
        for i in range(1, string_length):
            if string_length % i == 0:
                if s[:i] * (string_length // i) == s:
                    return True
        return False