class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # Know number of rows and columns will be the same
        num_rows = len(grid)
        num_cols = num_rows
        # Sum up max of each row
        # Sum up max of each column
        # Add row * column
        curr_area = 0
        col_max = [0] * num_cols
        for i in range(num_rows):
            row_max = 0
            for j in range(num_cols):
                row_max = max(row_max, grid[i][j])
                col_max[j] = max(col_max[j], grid[i][j])
                if grid[i][j] > 0:
                    curr_area += 1
            curr_area += row_max
        curr_area += sum(col_max)
        return curr_area