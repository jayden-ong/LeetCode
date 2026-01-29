class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        num_rows = len(grid)
        num_cols = len(grid[0])
        for i in range(num_rows):
            for j in range(num_cols):
                if i + 1 < num_rows:
                    if grid[i + 1][j] != grid[i][j]:
                        return False
                
                if j + 1 < num_cols:
                    if grid[i][j + 1] == grid[i][j]:
                        return False
        return True