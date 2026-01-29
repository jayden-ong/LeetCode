class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        curr = ""
        for word in words:
            curr += word
            if curr == s:
                return True
        return False