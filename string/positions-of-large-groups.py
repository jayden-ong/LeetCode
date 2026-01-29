class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        length_s = len(s)
        curr_streak = 1
        starting_character = s[0]
        beginning = 0
        large_group = []
        for i in range(1, length_s):
            if s[i] == starting_character:
                curr_streak += 1
            else:
                if curr_streak >= 3:
                    large_group.append([beginning, i - 1])
                curr_streak = 1
                starting_character = s[i]
                beginning = i
        
        if curr_streak >= 3:
            large_group.append([beginning, length_s - 1])
        return large_group
        