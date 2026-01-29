class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0
        answer = 0
        i = 1
        while i * i <= n:
            answer += 1
            i += 1
        return answer