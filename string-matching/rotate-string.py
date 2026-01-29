class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # abcde -> eabcd -> deabc -> cdeab -> bcdea -> abcde
        # First check if they are the same length
        length_s = len(s)
        length_goal = len(goal)

        if length_s != length_goal:
            return False
        
        # We know their lengths must be at least one
        letter_to_find = s[0]
        i = 0

        while i < length_goal:
            if goal[i:] == s[:length_goal - i] and goal[:i] == s[length_goal - i:]:
                return True
            i += 1
        
        # One of the letters does not appear
        return False
