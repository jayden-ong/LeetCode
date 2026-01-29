class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0])
        
        already_visited = set()
        waiting_to_visit = [(grid[-1][-1], len(grid) - 1, len(grid[0]) - 1)]
        while True:
            # We set the current water level to the current minimum one required to make progress
            curr_level = waiting_to_visit[0][0]
            while waiting_to_visit[0][0] <= curr_level:
                _, curr_row, curr_col = heapq.heappop(waiting_to_visit)
                # Add all directions that haven't already been visited
                for add_row, add_col in directions:
                    new_row, new_col = curr_row + add_row, curr_col + add_col
                    if (new_row, new_col) == (0, 0):
                        return max(grid[0][0], curr_level)
                    
                    if is_valid(new_row, new_col) and (new_row, new_col) not in already_visited:
                        heapq.heappush(waiting_to_visit, (grid[new_row][new_col], new_row, new_col))
                already_visited.add((curr_row, curr_col))

        # Should never run
        return -1