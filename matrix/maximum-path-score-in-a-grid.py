class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        dp = [[[-1] * (k + 1) for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # dp[row][col][s] stores the solution with the highest score with at most "s" cost
        for i in range(k + 1):
            dp[0][0][i] = 0
        
        cells_queue = deque()
        cells_queue.append((0, 0))
        queued = set()
        while cells_queue:
            curr_row, curr_col = cells_queue.popleft()
            add_cost = 0
            if grid[curr_row][curr_col] != 0:
                add_cost = 1
                
            # Have to use prev information to update the current cell
            if curr_row - 1 >= 0 and (curr_row, curr_col) != (0, 0):
                for old_k in range(k + 1):
                    if old_k < k and dp[curr_row - 1][curr_col][old_k] != -1 or grid[curr_row][curr_col] == 0:
                        dp[curr_row][curr_col][old_k + add_cost] = max(dp[curr_row][curr_col][old_k + add_cost], dp[curr_row - 1][curr_col][old_k] + grid[curr_row][curr_col])
            
            if curr_col - 1 >= 0 and (curr_row, curr_col) != (0, 0):
                for old_k in range(k + 1):
                    if old_k < k and dp[curr_row][curr_col - 1][old_k] != -1 or grid[curr_row][curr_col] == 0:
                        dp[curr_row][curr_col][old_k + add_cost] = max(dp[curr_row][curr_col][old_k + add_cost], dp[curr_row][curr_col - 1][old_k] + grid[curr_row][curr_col])

            if curr_row + 1 < len(grid) and (curr_row + 1, curr_col) not in queued:
                cells_queue.append((curr_row + 1, curr_col))
                queued.add((curr_row + 1, curr_col))
            
            if curr_col + 1 < len(grid[0]) and (curr_row, curr_col + 1) not in queued:
                cells_queue.append((curr_row, curr_col + 1))
                queued.add((curr_row, curr_col + 1))
        
        return max(dp[-1][-1])