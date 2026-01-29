class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # If all letters appear an even amount of times, it is wonderful
        # If two different letters show up an odd amount of times, not wonderful
        # abaa -> 
        # dp -> 1, 11 - 2 new strings to consider, add 1, 10 - 3 new strings to consider, add 2, 11 - 4 new strings to consider, add 2
        # a -> 01, aa -> 00, aaa -> 01, aaab -> 11
        # 1, 0, 1, 11
        # 11 ^ 01 = 10, 10 ^ 01 = 11 ^ 01 = 10
        # Can have at most one 1
        # Make a dictionary where the letter is the key and the value is how many times you 
        # have to shift the 1 bit and XOR with the mask
        num_wonderful = 0
        length_word = len(word)
        # Want a set with (number of odd occurrences, a set with all odd occurrences)
        letters_dict = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9}
        bitmask_dict = {}
        curr_mask = 0
        # By default, the 0 mask appears once
        bitmask_dict[0] = 1
        for i in range(length_word):
            # To get the next bitmask, XOR with previous
            # For every iteration, i + 1 new substrings have to be considered

            # If a mask appears more than once, then we can get a wonderful substring by 
            # creating a string that starts at the index of the occurrence of the mask + 1
            # and ending at another occurrence of the mask
            # If two masks are the same, all letters must appear an even amount of times
            # because the XOR of them is the parity of the substring between the masks
            curr_mask = curr_mask ^ (1 << letters_dict[word[i]])
            
            if curr_mask in bitmask_dict:
                num_wonderful += bitmask_dict[curr_mask]
            
            # If we alter one bit of the mask and we find that new version earlier, it means
            # we have another wonderful substring between those two masks because they only
            # differ by 1 bit, meaning there is at most one letter that shows up an odd amount
            # of times within that substring

            for letter in letters_dict:
                temp_mask = curr_mask ^ (1 << letters_dict[letter])
                if temp_mask in bitmask_dict:
                    num_wonderful += bitmask_dict[temp_mask]

            if curr_mask in bitmask_dict:
                bitmask_dict[curr_mask] += 1
            else:
                bitmask_dict[curr_mask] = 1
        return num_wonderful