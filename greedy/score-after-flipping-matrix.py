class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def flip(row):
            new_row = []
            for item in row:
                new_row.append(1 - item)
            return new_row
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        # Want to flip rows first
        for i in range(num_rows):
            if grid[i][0] == 0:
                grid[i] = flip(grid[i])
        #print(grid)

        answer = num_rows * pow(2, num_cols - 1)
        for j in range(1, num_cols):
            num_ones = 0
            for i in range(num_rows):
                if grid[i][j] == 1:
                    num_ones += 1
            
            answer += max(num_ones, num_rows - num_ones) * pow(2, num_cols - j - 1)
        return answer