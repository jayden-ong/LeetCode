class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # North and South should be the same?
        # East and West should be the same?
        row_maxes = []
        for row in grid:
            row_maxes.append(max(row))
        
        col_maxes = []
        for j in range(len(grid[0])):
            new_col = []
            for i in range(len(grid)):
                new_col.append(grid[i][j])
            col_maxes.append(max(new_col))
        
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                answer += min(row_maxes[i], col_maxes[j]) - grid[i][j]
        return answer