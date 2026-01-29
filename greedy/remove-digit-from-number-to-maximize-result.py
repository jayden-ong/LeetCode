class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        answer = 0
        length_number = len(number)
        for i in range(length_number):
            if number[i] == digit:
                answer = max(answer, int(number[:i] + number[i + 1:]))
        return str(answer)