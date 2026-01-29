class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        num_rows = len(grid)
        num_cols = len(grid[0])
        for i in range(num_rows):
            for j in range(num_cols):
                if (i == j or i + j == num_rows - 1):
                    if grid[i][j] == 0:
                        return False
                elif i != j and grid[i][j] != 0:
                    return False
        return True