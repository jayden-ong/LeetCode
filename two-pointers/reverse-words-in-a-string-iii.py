class Solution:
    def reverseWords(self, s: str) -> str:
        curr_string = ""
        words = s.split(" ")
        for word in words:
            curr_string = curr_string + word[::-1] + " "
        return curr_string.rstrip()