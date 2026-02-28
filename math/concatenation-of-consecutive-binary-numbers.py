class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        answer = 0
        curr_multiple = 1
        for i in range(n, 0, -1):
            answer += i * curr_multiple
            curr_multiple *= 2 ** (math.floor(math.log(i, 2)) + 1)
        return answer % MOD