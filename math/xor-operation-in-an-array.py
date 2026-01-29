class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        curr = 0
        answer = 0
        for i in range(n):
            curr = start + 2 * i
            answer ^= curr

        return answer