class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        alphabet_dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4,
                         'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8,
                         'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12,
                         'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16,
                         'q' : 17, 'r' : 18, 's' : 19, 't' : 20,
                         'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24,
                         'y' : 25, 'z' : 26}
        length_s = len(s)
        i = 0
        curr = 1
        last_letter = ""
        answers_dict = {}
        # If the longest ideal string is i + 1, it means the entire string up until i must be ideal
        while i < length_s:
            # For a string of length 1, it does satisfy the definition
            if i == 0:
                answers_dict[s[i]] = 1
            else:
                #print(answers_dict)
                # To make sure we don't use the new value when updating
                if s[i] in answers_dict:
                    old_val = answers_dict[s[i]]
                # By default the current character is 1 - it is possible for it to change                
                for key in answers_dict.copy():
                    # The longest ideal string that ends in s[i] increases by 1
                    if abs(alphabet_dict[s[i]] - alphabet_dict[key]) <= k:
                        #print(i)
                        #print(key)
                        #print(answers_dict)
                        #print('---')
                        if s[i] in answers_dict and s[i] != key:
                            answers_dict[s[i]] = max(answers_dict[s[i]], answers_dict.get(key, 0) + 1)
                        elif s[i] in answers_dict and s[i] == key:
                            answers_dict[s[i]] = max(answers_dict[s[i]], old_val + 1)
                        else:
                            answers_dict[s[i]] = answers_dict.get(key, 0) + 1
                        curr = max(answers_dict[s[i]], curr)
                        found_new_ending = True
                # If it is not in the dictionary, need to add it
                if s[i] not in answers_dict:
                    answers_dict[s[i]] = 1
            i += 1
        return curr