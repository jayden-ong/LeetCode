class Solution:
    def reverseVowels(self, s: str) -> str:
        string_length = len(s)
        curr_string = ""
        right = string_length - 1
        i = 0
        while i < string_length:
            if s[i] not in "aeiouAEIOU":
                curr_string += s[i]
            else:
                while s[right] not in "aeiouAEIOU":
                    right -= 1
                curr_string += s[right]
                right -= 1
            i += 1

        return curr_string
            

