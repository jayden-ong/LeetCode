class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        answer = [1] * n
        i = 2
        for i in range(2, int(pow(n, 0.5)) + 1):
            if answer[i] == 1:
                j = i + i
                while j < n:
                    answer[j] = 0
                    j += i
        return sum(answer) - 2