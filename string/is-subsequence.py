class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub_string_length = len(s)
        i = 0
        string_length = len(t)
        j = 0

        while i < sub_string_length and j < string_length:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == sub_string_length 
            