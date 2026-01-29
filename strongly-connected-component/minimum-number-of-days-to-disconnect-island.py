from collections import deque
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        diagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        num_rows, num_cols = len(grid), len(grid[0])
        def is_valid(i, j):
            return 0 <= i < num_rows and 0 <= j < num_cols
        
        # First, count number of islands -- if there are more than one islands, return 0
        # Need a function to determine if there is exactly one island
        def exactly_one(grid):
            tiles_explored = set()
            island_found = False
            for i in range(num_rows):
                for j in range(num_cols):
                    if grid[i][j] == 1:
                        if island_found and (i, j) not in tiles_explored:
                            # already found an island and an island not connected to original
                            return False
                        
                        # Want to perform search
                        queue = deque()
                        queue.append((i, j))
                        tiles_explored.add((i, j))
                        while queue:
                            curr_row, curr_col = queue.popleft()
                            for direction in directions:
                                new_row, new_col = curr_row + direction[0], curr_col + direction[1]
                                if is_valid(new_row, new_col) and (new_row, new_col) not in tiles_explored and grid[new_row][new_col] == 1:
                                    queue.append((new_row, new_col))
                                    tiles_explored.add((new_row, new_col))
                        island_found = True
            if not island_found:
                return False
            
            return True
        
        # No islands
        if not exactly_one(grid):
            return 0

        def count_land_adjacent(grid, i, j):
            answer = 0
            for direction in directions:
                new_row, new_col = i + direction[0], j + direction[1]
                if is_valid(new_row, new_col) and grid[new_row][new_col] == 1:
                    answer += 1
            return answer
        
        # If there is only one island, need to find min moves to make island into two
        # The goal is to isolate exactly one piece of land
        # There must be at least one piece of land that doesn't have land to the top and left
        # To show this start in the top left and go row by row
        # The first piece of land is the target

        # We only have to remove one if there is a piece of land if it connects two different components
        # This land must be connected to exactly two other pieces of land
        # Need to figure out a way to quickly check if land is still connected after removing one piece
        for i in range(num_rows):
            for j in range(num_cols):
                # If there is only one connection, it cannot possibly disconnect an island
                num_adjacent = count_land_adjacent(grid, i, j)
                if grid[i][j] == 1 and num_adjacent != 1:
                    if num_adjacent == 0:
                        return 1
                    

                    grid[i][j] = 0
                    if not exactly_one(grid):
                        return 1
                    grid[i][j] = 1

        return 2