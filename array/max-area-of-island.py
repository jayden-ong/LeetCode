from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        num_rows = len(grid)
        num_cols = len(grid[0])
        def is_valid(i, j):
            return 0 <= i < num_rows and 0 <= j < num_cols

        answer = 0
        # Will only contain tiles that contain 1
        visited = set()
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    curr_size = 1
                    # Want to do BFS
                    queue = deque()
                    queue.append((i, j))
                    visited.add((i, j))
                    while queue:
                        curr_row, curr_col = queue.popleft()
                        for direction in directions:
                            new_row, new_col = curr_row + direction[0], curr_col + direction[1]
                            if is_valid(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                                queue.append((new_row, new_col))
                                visited.add((new_row, new_col))
                                curr_size += 1
                    answer = max(curr_size, answer)
        return answer