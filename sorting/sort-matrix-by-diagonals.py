class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        starting_row, starting_col = len(grid) - 1, 0
        for j in range(2 * len(grid) - 1):
            nums = []
            curr_row, curr_col = starting_row, starting_col
            while curr_row < len(grid) and curr_col < len(grid[0]):
                nums.append(grid[curr_row][curr_col])
                curr_row, curr_col = curr_row + 1, curr_col + 1
            if j < len(grid):
                nums.sort(reverse=True)
            else:
                nums.sort()

            i = 0
            curr_row, curr_col = starting_row, starting_col
            while curr_row < len(grid) and curr_col < len(grid[0]):
                grid[curr_row][curr_col] = nums[i]
                curr_row, curr_col = curr_row + 1, curr_col + 1
                i += 1
            
            if starting_row == 0:
                starting_col += 1
            else:
                starting_row -= 1
        return grid