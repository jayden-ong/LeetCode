class Solution:
    def sortVowels(self, s: str) -> str:
        string_length = len(s)
        vowels_list = []
        for char in s:
            if char in "aeiouAEIOU":
                vowels_list.append(char)
        
        vowels_list = sorted(vowels_list, key=ord)
        new_string = ""
        i = 0
        for char in s:
            if char in "aeiouAEIOU":
                new_string += vowels_list[i]
                i += 1
            else:
                new_string += char
        
        return new_string