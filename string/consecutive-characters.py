class Solution:
    def maxPower(self, s: str) -> int:
        curr_char = s[0]
        curr_streak = 1
        answer = 1
        length_s = len(s)
        for i in range(1, length_s):
            if s[i] == curr_char:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_char = s[i]
            
            answer = max(answer, curr_streak)
            
        return answer