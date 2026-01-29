class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = []
        answer = 0
        for i in range(len(matrix)):
            new_row = []
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        new_row.append(1)
                    else:
                        temp = [dp[i - 1][j], dp[i - 1][j - 1], new_row[-1]]
                        new_row.append(min(temp) + 1)
                else:
                    new_row.append(0)
                answer += new_row[-1]
            dp.append(new_row)
        return answer
                        
