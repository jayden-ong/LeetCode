from collections import deque
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0])

        curr_obstacles_broken = 0
        dp = []
        for i in range(len(grid)):
            new_row = []
            for j in range(len(grid[0])):
                new_row.append(float('inf'))
            dp.append(new_row)
        
        curr_queue = deque()
        curr_queue.append((0, 0))
        cells_explored = set()
        cells_explored.add((0, 0))
        # Will contain cells that required an additional obstacle to be broken
        broken_obstacles_queue = deque()
        
        while True:
            while curr_queue:
                curr_row, curr_col = curr_queue.popleft()
                dp[curr_row][curr_col] = min(dp[curr_row][curr_col], curr_obstacles_broken)
                # If we see the target, we would have gotten there with minimum obstacles broken
                if curr_row == len(grid) - 1 and curr_col == len(grid[0]) - 1:
                    return dp[curr_row][curr_col]
                
                for add_row, add_col in directions:
                    new_row, new_col = curr_row + add_row, curr_col + add_col
                    if is_valid(new_row, new_col) and (new_row, new_col) not in cells_explored:
                        cells_explored.add((new_row, new_col))
                        if grid[new_row][new_col] == 0:
                            curr_queue.append((new_row, new_col))
                        else:
                            broken_obstacles_queue.append((new_row, new_col))
            
            curr_queue = broken_obstacles_queue
            broken_obstacles_queue = deque()
            curr_obstacles_broken += 1
        