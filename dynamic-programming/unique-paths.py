from collections import deque
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer = []
        for i in range(m):
            new_row = [1] * n
            if i > 0:
                for j in range(n):
                    if j == 0:
                        new_row[j] = 1
                    else:
                        new_row[j] = new_row[j - 1] + answer[i - 1][j]
            answer.append(new_row)
        return answer[-1][-1]