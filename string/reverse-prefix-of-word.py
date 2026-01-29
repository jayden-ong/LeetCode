class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        string_to_reverse = ""
        for i in range(len(word)):
            if word[i] == ch:
                string_to_reverse += word[i]
                return string_to_reverse[::-1] + word[i + 1:]
            else:
                string_to_reverse += word[i]
        return word