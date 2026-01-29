class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        num_rows = len(land)
        num_cols = len(land[0])
        answer = []
        i = 0
        j = 0
        while i < num_rows:
            j = 0
            while j < num_cols:
                # Need to find bottom right corner
                # If going left to right, up to down, only have to go right and down
                if land[i][j] == 1:
                    # Need to check answer to ensure land is not already included
                    # Check left and up
                    # If 1, it means it was already included in previous land
                    if (i > 0 and land[i - 1][j] == 1) or (j > 0 and land[i][j - 1] == 1):
                        j += 1
                    else:
                        starting_col = j
                        starting_row = i
                        # Go right
                        while starting_col < num_cols and land[i][starting_col] == 1:
                            starting_col += 1
                        # Need to go 1 back to the left
                        starting_col -= 1
                        while starting_row < num_rows and land[starting_row][starting_col] == 1:
                            starting_row += 1
                        starting_row -= 1
                        answer.append([i, j, starting_row, starting_col])
                        # We can skip?
                        j = starting_col + 1
                else:
                    j += 1
            i += 1
        return answer