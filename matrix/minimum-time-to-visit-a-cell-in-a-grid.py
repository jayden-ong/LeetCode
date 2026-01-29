class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] >= 2 and grid[1][0] >= 2:
            return -1
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0])
        
        # visited_squares contains all cells that have already been visited
        visited_squares = set()
        # Contains all squares that need to be explored
        squares_queue = []
        heapq.heappush(squares_queue, (0, 0, 0))
        while squares_queue:
            curr_time, curr_row, curr_col = heapq.heappop(squares_queue)
            # We have arrived
            if curr_row == len(grid) - 1 and curr_col == len(grid[0]) - 1:
                return curr_time

            if (curr_row, curr_col) not in visited_squares:
                for add_row, add_col in directions:
                    new_row, new_col = add_row + curr_row, add_col + curr_col
                    if is_valid(new_row, new_col) and (new_row, new_col) not in visited_squares:
                        if curr_time + 1 >= grid[new_row][new_col]:
                            heapq.heappush(squares_queue, (curr_time + 1, new_row, new_col))
                        else:
                            # Can go back and forth to get onto next square
                            time_diff = grid[new_row][new_col] - curr_time
                            # diff is even, grid[new_row][new_col] + 1
                            # diff is odd, grid[new_row][new][col]
                            if time_diff % 2 == 0:
                                heapq.heappush(squares_queue, (grid[new_row][new_col] + 1, new_row, new_col))
                            else:
                                heapq.heappush(squares_queue, (grid[new_row][new_col], new_row, new_col))
            visited_squares.add((curr_row, curr_col))
        return -1
                