class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        answer = 0
        length_num1 = len(num1)
        length_num2 = len(num2)
        num_zeros = 0
        for i in range(length_num2 - 1, -1, -1):
            res = str(int(num2[i]) * int(num1)) + '0' * num_zeros
            answer += int(res)
            num_zeros += 1
        return str(answer)