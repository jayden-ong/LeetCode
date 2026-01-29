class Solution:
    def countDigits(self, num: int) -> int:
        string_num = str(num)
        answer = 0
        for digit in string_num:
            if num % int(digit) == 0:
                answer += 1
        return answer