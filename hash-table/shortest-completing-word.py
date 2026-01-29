class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters_dict = {}
        num_chars_to_use = 0
        for char in licensePlate:
            if char.isalpha():
                if char.lower() not in letters_dict:
                    letters_dict[char.lower()] = 1
                else:
                    letters_dict[char.lower()] += 1
                num_chars_to_use += 1
        
        curr_shortest = -1
        curr_cand = None
        for word in words:
            new_dict = letters_dict.copy()
            num_letters_required = num_chars_to_use
            for char in word:
                if char in new_dict and new_dict[char] > 0:
                    new_dict[char] -= 1
                    num_letters_required -= 1
                
                if num_letters_required == 0:
                    if curr_shortest == -1 or len(word) < curr_shortest:
                        curr_shortest = len(word)
                        curr_cand = word
                    break
        return curr_cand
