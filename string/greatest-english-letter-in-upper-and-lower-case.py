class Solution:
    def greatestLetter(self, s: str) -> str:
        curr_greatest = ""
        letters_appeared = set()
        for char in s:
            letters_appeared.add(char)
            # If uppercase, check if lowercase has appeared
            if char.isupper():
                if char.lower() in letters_appeared and (curr_greatest == "" or char > curr_greatest):
                    curr_greatest = char
            else:
                if char.upper() in letters_appeared and (curr_greatest == "" or char.upper() > curr_greatest):
                    curr_greatest = char.upper()
        return curr_greatest

