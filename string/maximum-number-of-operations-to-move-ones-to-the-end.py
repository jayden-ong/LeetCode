class Solution:
    def maxOperations(self, s: str) -> int:
        num_ones = 0
        answer = 0
        for i, digit in enumerate(s):
            if digit == "1":
                if i > 0 and s[i - 1] == "0":
                    answer += num_ones
                num_ones += 1
            else:
                if i == len(s) - 1:
                    answer += num_ones
        return answer