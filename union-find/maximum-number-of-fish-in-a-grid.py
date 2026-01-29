from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0])
        cells_explored = set()

        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0 and (i, j) not in cells_explored:
                    water_queue = deque()
                    water_queue.append((i, j))
                    cells_explored.add((i, j))
                    curr_score = 0
                    while water_queue:
                        curr_row, curr_col = water_queue.popleft()
                        curr_score += grid[curr_row][curr_col]
                        for add_row, add_col in directions:
                            new_row, new_col = curr_row + add_row, curr_col + add_col
                            if is_valid(new_row, new_col) and (new_row, new_col) not in cells_explored and grid[new_row][new_col] > 0:
                                water_queue.append((new_row, new_col))
                                cells_explored.add((new_row, new_col))
                    answer = max(answer, curr_score)
        return answer