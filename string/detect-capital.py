class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_capital = True
        all_lowercase = True
        first_uppercase = True
        first = True
        for char in word:
            if first:
                if char.isupper():
                    all_lowercase = False
                else:
                    all_capital = False
                    first_uppercase = False
                first = False
            else:
                if char.isupper():
                    first_uppercase = False
                    all_lowercase = False
                else:
                    all_capital = False
        return first_uppercase or all_lowercase or all_capital