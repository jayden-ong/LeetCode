class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        perimeter = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    # Automatically add 1 because of the top
                    if i != 0:
                        if grid[i - 1][j] == 0:
                            perimeter += 1
                    else:
                        perimeter += 1
                    
                    # Need to look at tile below
                    if i != num_rows - 1:
                        if grid[i + 1][j] == 0:
                            perimeter += 1
                    else:
                        # Automatically add 1 because of bottom
                        perimeter += 1
                    
                    # Need to check left column
                    if j != 0:
                        if grid[i][j - 1] == 0:
                            perimeter += 1
                    else:
                        # Automatically add 1 because of the left
                        perimeter += 1
                    
                    # Need to look at tile to the right
                    if j != num_cols - 1:
                        if grid[i][j + 1] == 0:
                            perimeter += 1
                    else:
                        # Automatically add 1 because of the right
                        perimeter += 1
        return perimeter