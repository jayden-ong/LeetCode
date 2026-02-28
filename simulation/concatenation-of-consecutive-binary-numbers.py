class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        str_n = ""
        for i in range(1, n + 1):
            str_n += format(i, 'b')
        answer = 0
        for i in range(len(str_n)):
            answer += pow(2, i) * int(str_n[len(str_n) - 1 - i])
        return answer % MOD