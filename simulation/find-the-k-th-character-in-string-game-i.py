class Solution:
    def kthCharacter(self, k: int) -> str:
        def convert_next(word):
            curr = ""
            for letter in word:
                if letter == "z":
                    curr += "a"
                else:
                    curr += chr(ord(letter) + 1)
            return curr
        curr = "a"
        while len(curr) < k:
            curr = curr + convert_next(curr)
        return curr[k - 1]