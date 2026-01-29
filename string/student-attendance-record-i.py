class Solution:
    def checkRecord(self, s: str) -> bool:
        num_absent = 0
        curr_streak = 0
        for char in s:
            if char == 'P':
                curr_streak = 0
            elif char == 'A':
                curr_streak = 0
                num_absent += 1
            else:
                curr_streak += 1
                if curr_streak >= 3:
                    return False
        return num_absent < 2
