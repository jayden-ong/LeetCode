class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        curr_res = []
        for word in words:
            # Want to figure out which row of keyboard we are on
            if word[0] in "qwertyuiopQWERTYUIOP":
                row = "qwertyuiopQWERTYUIOP"
            elif word[0] in "asdfghjklASDFGHJKL":
                row = "asdfghjklASDFGHJKL"
            else:
                row = "zxcvbnmZXCVBNM"
            
            valid = True
            for char in word:
                if char not in row:
                    valid = False
                    break
            
            if valid:
                curr_res.append(word)
        return curr_res