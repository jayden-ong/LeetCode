class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # Will return the maximum amount of gold starting at curr_row, curr_col
        def dfs(curr_row, curr_col):
            old_gold = grid[curr_row][curr_col]
            answer = 0
            grid[curr_row][curr_col] = 0
            if curr_row > 0 and grid[curr_row - 1][curr_col] != 0:
                answer = max(answer, dfs(curr_row - 1, curr_col))
            
            if curr_row < num_rows - 1 and grid[curr_row + 1][curr_col] != 0:
                answer = max(answer, dfs(curr_row + 1, curr_col))
                        
            if curr_col > 0 and grid[curr_row][curr_col - 1] != 0:
                answer = max(answer, dfs(curr_row, curr_col - 1))

            if curr_col < num_cols - 1 and grid[curr_row][curr_col + 1] != 0:
                answer = max(answer, dfs(curr_row, curr_col + 1))
            grid[curr_row][curr_col] = old_gold
            return answer + old_gold

        num_rows = len(grid)
        num_cols = len(grid[0])
        answer = 0
        for i in range(num_rows):
            for j in range(num_cols):
                # Do DFS
                if grid[i][j] != 0:
                    res = dfs(i, j)
                    #print(res)
                    answer = max(answer, res)
                    #print('---')
                    
        return answer

