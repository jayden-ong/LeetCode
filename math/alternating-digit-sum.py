class Solution:
    def alternateDigitSum(self, n: int) -> int:
        string_n = str(n)
        answer = 0
        modifier = 1
        for char in string_n:
            answer += int(char) * modifier
            modifier *= -1
        return answer