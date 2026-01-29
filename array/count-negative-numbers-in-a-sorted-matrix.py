class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        answer = 0
        last_col = num_cols
        for i in range(num_rows):
            for j in range(last_col):
                if grid[i][j] < 0:
                    answer += (last_col - j) * (num_rows - i)
                    last_col = j
                    break
        return answer