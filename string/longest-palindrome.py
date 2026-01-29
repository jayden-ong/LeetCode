class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters_dict = {}
        for char in s:
            letters_dict[char] = letters_dict.get(char, 0) + 1
        
        longest_pal = 0
        longest_odd = 0
        # Can only have 1 odd amount of letters
        found_one = False
        num_to_remove = 0
        for key in letters_dict:
            if letters_dict[key] == 1 and not found_one:
                found_one = True
                longest_pal += 1
            elif letters_dict[key] % 2 == 0:
                longest_pal += letters_dict[key]
            else:
                # Might have to remove 1 letter from each odd amount of letters
                longest_pal += letters_dict[key]
                num_to_remove += 1
        
        if found_one:
            return longest_pal - num_to_remove
        else:
            if num_to_remove == 0:
                return longest_pal
            else:
                return longest_pal - num_to_remove + 1