class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        answer = 0
        curr_multiple = 1
        for i in range(n, 0, -1):
            answer += i * curr_multiple
            curr_multiple *= pow(2, len(format(i, 'b')))
        return answer % MOD