from collections import deque
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # At any given cell, can move right and up/down/stay
        # The maximum number of moves is capped at the number of columns
        dp = []
        num_rows = len(grid)
        num_cols = len(grid[0])
        cell_queue = deque()
        # If we've reached a tile that has already been reached using a previous path, no point in exploring it
        for i in range(num_rows):
            new_row = [False] * num_cols
            dp.append(new_row)
            cell_queue.append((i, 0))
            dp[i][0] = True
        
        answer = 0
        while cell_queue:
            curr_row, curr_col = cell_queue.popleft()
            answer = max(answer, curr_col)
            if answer == num_cols - 1:
                return answer
            curr_val = grid[curr_row][curr_col]
            # Check up if we can actually go there and we have not already visited it
            if curr_row > 0 and grid[curr_row - 1][curr_col + 1] > curr_val and not dp[curr_row - 1][curr_col + 1]:
                cell_queue.append((curr_row - 1, curr_col + 1))
                dp[curr_row - 1][curr_col + 1] = True

            # Check right
            if grid[curr_row][curr_col + 1] > curr_val and not dp[curr_row][curr_col + 1]:
                cell_queue.append((curr_row, curr_col + 1))
                dp[curr_row][curr_col + 1] = True
            
            # Check down
            if curr_row < num_rows - 1 and grid[curr_row + 1][curr_col + 1] > curr_val and not dp[curr_row + 1][curr_col + 1]:
                cell_queue.append((curr_row + 1, curr_col + 1))
                dp[curr_row + 1][curr_col + 1] = True

        return answer
