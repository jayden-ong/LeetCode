class Solution:
    def toLowerCase(self, s: str) -> str:
        curr_string = ""
        for char in s:
            if char.isupper():
                curr_string += char.lower()
            else:
                curr_string += char
        return curr_string