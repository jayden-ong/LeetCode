class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        # When we see zero, start a streak
        zero_streak = 0
        one_streak = 0
        answer = 0
        saved_zero_streak = 0
        for char in s:
            if char == '0':
                zero_streak += 1
                if one_streak > 0:
                    answer = max(answer, 2 * min(saved_zero_streak, one_streak))
                    saved_zero_streak = 0
                one_streak = 0
            else:
                one_streak += 1
                if zero_streak > 0:
                    saved_zero_streak = zero_streak
                zero_streak = 0
        
        answer = max(answer, 2 * min(saved_zero_streak, one_streak))
        return answer