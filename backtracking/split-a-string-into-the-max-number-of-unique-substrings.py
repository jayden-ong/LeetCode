class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def string_split(curr_index, curr_string, curr_set):
            if curr_index == len(s):
                if curr_string == "":
                    return len(curr_set)
                else:
                    if curr_string in curr_set:
                        return 0
                    return len(curr_set) + 1
            
            # Two options 
            # 1. Add current letter to the current string which means do not add it to set
            first_option = string_split(curr_index + 1, curr_string + s[curr_index], curr_set.copy())

            # 2. Add current string to the set and have the next letter be the start of the new substring
            new_set = curr_set.copy()
            second_option = -1
            if curr_string != "" and curr_string not in new_set:
                new_set.add(curr_string)
                second_option = string_split(curr_index + 1, s[curr_index], new_set)
            
            return max(first_option, second_option)
        return string_split(0, "", set())