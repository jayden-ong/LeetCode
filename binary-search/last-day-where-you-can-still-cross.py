class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # We can figure out when it becomes impossible to go from top to bottom
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < row and 0 <= curr_col < col

        def is_possible(curr_day):
            water_cells = set()
            # Add all water tiles
            for water_row, water_col in cells[:curr_day]:
                water_cells.add((water_row - 1, water_col - 1))
            
            visited = set()
            cell_queue = deque()
            # Add all possible starting spaces
            for j in range(col):
                if (0, j) not in water_cells:
                    cell_queue.append((0, j))
                    visited.add((0, j))
            
            while cell_queue:
                curr_row, curr_col = cell_queue.popleft()
                for add_row, add_col in directions:
                    new_row, new_col = curr_row + add_row, curr_col + add_col
                    if is_valid(new_row, new_col) and (new_row, new_col) not in visited and (new_row, new_col) not in water_cells:
                        # No point in exploring further if we have added the goal
                        if new_row == row - 1:
                            return True
                        visited.add((new_row, new_col))
                        cell_queue.append((new_row, new_col))

            return False
        
        # Use binary search to rule out options quickly
        answer = 0
        left, right = 0, row * col
        while left < right:
            mid = (left + right) // 2
            if is_possible(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid
        return answer