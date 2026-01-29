class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        if not word.isalnum():
            return False
        
        consonant = False
        vowel = False
        for letter in word:
            if letter.isalpha():
                if letter in "aeiouAEIOU":
                    vowel = True
                else:
                    consonant = True
        return vowel and consonant