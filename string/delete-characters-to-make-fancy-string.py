class Solution:
    def makeFancyString(self, s: str) -> str:
        new_string = ""
        length_s = len(s)
        curr_streak = 1
        curr_char = s[0]
        new_string = s[0]

        for i in range(1, length_s):
            if curr_char == s[i]:
                # Do not add character if streak is at least 3
                curr_streak += 1
                if curr_streak < 3:
                    new_string += s[i]
                    
            else:
                new_string += s[i]
                curr_streak = 1
                curr_char = s[i]
        return new_string

