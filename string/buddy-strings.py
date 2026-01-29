class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        length_s = len(s)
        length_goal = len(goal)
        if length_s != length_goal:
            return False
        
        first_index = None
        second_index = None
        i = 0
        num_diff = 0
        letters_dict = {}
        can_swap_same = False
        for i in range(length_s):
            if s[i] not in letters_dict:
                letters_dict[s[i]] = 1
            else:
                letters_dict[s[i]] += 1
                can_swap_same = True

            if s[i] != goal[i]:
                if first_index is None:
                    first_index = i
                elif second_index is None:
                    second_index = i
                num_diff += 1
            
        if num_diff == 0 and can_swap_same:
            return True
        
        if num_diff != 2:
            return False
        
        return s[first_index] == goal[second_index] and s[second_index] == goal[first_index]