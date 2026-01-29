class Solution:
    def doesAliceWin(self, s: str) -> bool:
        num_vowels = 0
        num_cons = 0
        for char in s:
            if char in "aeiou":
                num_vowels += 1
            else:
                num_cons += 1
        
        # Alice would just have to take all but one vowel
        if num_vowels == 0:
            return False
        
        return True
        
        # Alice always has to take at least one vowel
        # Alice has to make sure there isn't an even amount of vowels at the end of her turn
        #   Otherwise, Bob can take all of the letters and she loses