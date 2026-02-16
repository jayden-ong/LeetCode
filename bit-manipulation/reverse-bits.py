class Solution:
    def reverseBits(self, n: int) -> int:
        binary_s = format(n, 'b')
        if len(binary_s) < 32:
            binary_s = "0" * (32 - len(binary_s)) + binary_s
        answer = 0
        for i in range(len(binary_s)):
            answer += pow(2, i) * int(binary_s[i])
        return answer