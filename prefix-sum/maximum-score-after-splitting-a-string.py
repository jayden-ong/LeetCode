class Solution:
    def maxScore(self, s: str) -> int:
        left_zeros = 0
        right_ones = 0
        # Setup
        for char in s:
            if char == "1":
                right_ones += 1
        
        length_s = len(s)
        answer = 0
        for i in range(length_s - 1):
            if s[i] == "0":
                left_zeros += 1
            else:
                right_ones -= 1
            answer = max(answer, left_zeros + right_ones)
        return answer