class Solution:
    def countTriples(self, n: int) -> int:
        answer = 0
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                for k in range(j + 1, n + 1):
                    if pow(i, 2) + pow(j, 2) == pow(k, 2):
                        answer += 2
        return answer