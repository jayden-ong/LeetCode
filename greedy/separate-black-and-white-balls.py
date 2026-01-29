class Solution:
    def minimumSteps(self, s: str) -> int:
        # All 0's need to be to the left
        # All 1's need to be to the right
        # Represents where the next black ball has to go
        curr_pos = 0
        answer = 0
        for i in range(len(s)):
            ball = s[i]
            if ball == "0":
                answer += i - curr_pos
                curr_pos += 1
        return answer
                