class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # row 0, row 1, row 2, col 0, col 1, col 2, diag top left, diag top right
        magic_square_data = [0] * 8
        answer = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                # Need to count number of unique vals (should be 9)
                unique_val_set = set()
                unique_val_set.add(grid[i][j])
                unique_val_set.add(grid[i + 1][j])
                unique_val_set.add(grid[i + 2][j])
                unique_val_set.add(grid[i][j + 1])
                unique_val_set.add(grid[i + 1][j + 1])
                unique_val_set.add(grid[i + 2][j + 1])
                unique_val_set.add(grid[i][j + 2])
                unique_val_set.add(grid[i + 1][j + 2])
                unique_val_set.add(grid[i + 2][j + 2])
                if len(unique_val_set) == 9 and max(unique_val_set) < 10 and min(unique_val_set) > 0:
                    # All rows
                    magic_square_data[0] = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                    magic_square_data[1] = grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2]
                    magic_square_data[2] = grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                    magic_square_data[3] = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
                    magic_square_data[4] = grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]
                    magic_square_data[5] = grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]
                    magic_square_data[6] = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
                    magic_square_data[7] = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]
                    if [magic_square_data[0]] * 8 == magic_square_data:
                        answer += 1
        return answer
                