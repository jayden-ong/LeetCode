class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    stack = [(i, j)]
                    while stack:
                        row, col = stack.pop()
                        visited[(row, col)] = 0
                        # Have to check all four directions
                        if row > 0 and grid[row - 1][col] == "1" and visited.get((row - 1, col), -1) != 0:
                            # Add up
                            stack.append((row - 1, col))
                        if row < num_rows - 1 and grid[row + 1][col] == "1" and visited.get((row + 1, col), -1) != 0:
                            # Add down
                            stack.append((row + 1, col))
                        if col < num_cols - 1 and grid[row][col + 1] == "1" and visited.get((row, col + 1), -1) != 0:
                            # Add right
                            stack.append((row, col + 1))
                        if col > 0 and grid[row][col - 1] == "1" and visited.get((row, col - 1), -1) != 0:
                            # Add left
                            stack.append((row, col - 1))
                    num_islands += 1
        return num_islands