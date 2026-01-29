class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # want to get the index of every character in "s"
        # loop over all characters of "t" and once we cant find
        # the index, return the number of characters subtracted by index
        s_dict = {}
        k = 0
        for char in s:
            if char not in s_dict:
                s_dict[char] = [[k], 0]
            else:
                s_dict[char][0].append(k)
            k += 1
        
        prev_pos = float('-inf')
        for i in range(len(t)):
            if t[i] not in s_dict:
                return len(t) - i
            else:
                curr_index = s_dict[t[i]][1]
                curr_list = s_dict[t[i]][0]
                while curr_index < len(curr_list) and curr_list[curr_index] < prev_pos:
                    curr_index += 1
                
                if curr_index >= len(curr_list):
                    return len(t) - i
                
                prev_pos = curr_list[curr_index]
                curr_index += 1
                s_dict[t[i]][1] = curr_index
                
        return 0