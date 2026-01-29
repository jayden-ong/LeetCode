class Solution:
    def equalFrequency(self, word: str) -> bool:
        letter_dict = {}
        num_unique_letters = 0
        most_freq_letter = ""
        num_appear = 0
        for char in word:
            if char in letter_dict:
                letter_dict[char] += 1
                if letter_dict[char] > num_appear:
                    num_appear = letter_dict[char]
                    most_freq_letter = char
            else:
                letter_dict[char] = 1
                num_unique_letters += 1
                if most_freq_letter == "":
                    num_appear = 1
                    most_freq_letter = char
        
        # One frequency should be one more than all the other frequencies
        if num_unique_letters == 1 or num_appear == 1:
            return True
        
        # Return true if all letters appear same amount of time, except for 1 which appears once
        num_freq_one = 0
        valid = True
        for letter in letter_dict:
            if letter_dict[letter] == 1:
                num_freq_one += 1
                if num_freq_one > 1:
                    valid = False
                    break
            else:
                if letter_dict[letter] != num_appear:
                    valid = False
                    break
        
        if num_freq_one == 1 and valid:
            return True
        # Return true if all letters appear same amount of time, except for 1 which appears one more time
        for letter in letter_dict:
            if letter_dict[letter] == num_appear and letter != most_freq_letter:
                return False
            
            if letter_dict[letter] + 1 != num_appear and letter != most_freq_letter:
                return False
        return True