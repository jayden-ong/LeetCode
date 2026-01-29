class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        answer = []
        num_rows = len(grid)
        num_cols = len(grid[0])
        for i in range(num_rows):
            new_row = []
            for j in range(num_cols):
                if i == 0 and j == 0:
                    new_row.append(grid[i][j])
                elif i == 0:
                    new_row.append(grid[i][j] + new_row[j - 1])
                elif j == 0:
                    new_row.append(grid[i][j] + answer[i - 1][j])
                else:
                    new_row.append(grid[i][j] + min(answer[i - 1][j], new_row[j - 1]))
            answer.append(new_row)
        return answer[-1][-1]
