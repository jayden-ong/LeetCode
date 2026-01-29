class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        leftmost_column = float('inf')
        rightmost_column = float('-inf')
        highest_row = float('inf')
        lowest_row = float('-inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    leftmost_column = min(leftmost_column, j)
                    rightmost_column = max(rightmost_column, j)
                    highest_row = min(highest_row, i)
                    lowest_row = max(lowest_row, i)
        return (rightmost_column - leftmost_column + 1) * (lowest_row - highest_row + 1)