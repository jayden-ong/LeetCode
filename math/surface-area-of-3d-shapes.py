class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # Want to get maximum of each column
        # Want to get maximum of each row
        # Know number of rows and columns will be the same
        num_rows = len(grid)
        num_cols = len(grid[0])
        curr_area = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] > 0:
                    curr_area += 2
                
                if i == 0:
                    curr_area += grid[i][j]
                if i == num_rows - 1:
                    curr_area += grid[i][j]
                if j == 0:
                    curr_area += grid[i][j]
                if j == num_cols - 1:
                    curr_area += grid[i][j]
                
                # Have to check all around
                if i > 0 and grid[i - 1][j] > grid[i][j]:
                    curr_area += grid[i - 1][j] - grid[i][j]
                    
                if i < num_rows - 1 and grid[i + 1][j] > grid[i][j]:
                    curr_area += grid[i + 1][j] - grid[i][j]
                    
                if j > 0 and grid[i][j - 1] > grid[i][j]:
                    curr_area += grid[i][j - 1] - grid[i][j]
                    
                if j < num_cols - 1 and grid[i][j + 1] > grid[i][j]:
                    curr_area += grid[i][j + 1] - grid[i][j]
                    
            
        return curr_area