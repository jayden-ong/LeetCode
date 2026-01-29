class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        row_sum = [[0] * len(grid[0]) for _ in range(len(grid))]
        col_sum = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            curr = 0
            for j in range(len(grid[0])):
                curr += grid[i][j]
                row_sum[i][j] = curr
            
        for j in range(len(grid[0])):
            curr = 0
            for i in range(len(grid)):
                curr += grid[i][j]
                col_sum[i][j] = curr
        
        # Start with largest possible length
        for length in range(min(len(grid), len(grid[0])), 1, -1):
            # i, j represents the top left corner of the square we are checking
            for i in range(len(grid) - length + 1):
                for j in range(len(grid[0]) - length + 1):
                    # All rows/columns/diagonals must be the same -- take first row
                    test_sum = row_sum[i][j + length - 1]
                    if j > 0:
                        test_sum -= row_sum[i][j - 1]
                    
                    valid = True
                    # Check rows
                    for i2 in range(i, i + length):
                        curr_sum = row_sum[i2][j + length - 1]
                        if j > 0:
                            curr_sum -= row_sum[i2][j - 1]
                        
                        if curr_sum != test_sum:
                            valid = False
                            break
                    if not valid:
                        continue
                    
                    # Check cols
                    for j2 in range(j, j + length):
                        curr_sum = col_sum[i + length - 1][j2]
                        if i > 0:
                            curr_sum -= col_sum[i - 1][j2]
                        
                        if curr_sum != test_sum:
                            valid = False
                            break
                    if not valid:
                        continue
                    
                    # Check diags
                    d1 = d2 = 0
                    for k in range(length):
                        d1 += grid[i + k][j + k]
                        d2 += grid[i + k][j + length - 1 - k]
                    
                    if d1 == test_sum and d2 == test_sum:
                        return length
        return 1