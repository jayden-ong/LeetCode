from collections import deque
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0])
        
        # Want to find all the islands
        # Maps (row, col) to the island it belongs to
        coords_to_islands = {}
        # Maps each island to the size
        islands_to_size = []
        island_index = 0
        water_cells = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in coords_to_islands:
                    cells_queue = deque()
                    cells_queue.append((i, j))
                    cells_in_island = set()
                    cells_in_island.add((i, j))
                    coords_to_islands[(i, j)] = island_index
                    while cells_queue:
                        curr_row, curr_col = cells_queue.popleft()
                        for add_row, add_col in directions:
                            new_row, new_col = curr_row + add_row, curr_col + add_col
                            if is_valid(new_row, new_col) and grid[new_row][new_col] == 1 and (new_row, new_col) not in coords_to_islands:
                                coords_to_islands[(new_row, new_col)] = island_index
                                cells_queue.append((new_row, new_col))
                                cells_in_island.add((new_row, new_col))
                    islands_to_size.append(len(cells_in_island))
                    island_index += 1

                if grid[i][j] == 0:
                    water_cells.append((i, j))
        
        answer = 0
        if len(islands_to_size) > 0:
            answer = max(islands_to_size)
        
        for water_row, water_col in water_cells:
            islands_used = set()
            curr_score = 1
            for add_row, add_col in directions:
                new_row, new_col = water_row + add_row, water_col + add_col
                if (new_row, new_col) in coords_to_islands and coords_to_islands[(new_row, new_col)] not in islands_used:
                    curr_score += islands_to_size[coords_to_islands[(new_row, new_col)]]
                    islands_used.add(coords_to_islands[(new_row, new_col)])
            answer = max(answer, curr_score)
        return answer
            

        