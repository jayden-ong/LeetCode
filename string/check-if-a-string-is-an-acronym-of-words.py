class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        new_string = ""
        for word in words:
            new_string += word[0]
        
        return new_string == s