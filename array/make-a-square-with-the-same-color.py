class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        def check_square(row, col):
            stats = {"B" : 0, "W" : 0}
            stats[grid[row][col]] += 1
            stats[grid[row + 1][col]] += 1
            stats[grid[row][col + 1]] += 1
            stats[grid[row + 1][col + 1]] += 1
            return stats["B"] >= 3 or stats["W"] >= 3

        num_rows = len(grid)
        num_cols = len(grid[0])
        for i in range(num_rows - 1):
            for j in range(num_cols - 1):
                if check_square(i, j):
                    return True
        return False