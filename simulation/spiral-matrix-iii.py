class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = ["right", "down", "left", "up"]
        def perform_check(curr_row, curr_col):
            return 0 <= curr_row < rows and 0 <= curr_col < cols
        
        # Always start heading to the right
        # Whenever you get left or right, increase step size by 1
        answer = [[rStart, cStart]]
        direction_index = 0
        curr_row, curr_col = rStart, cStart
        step_size = 0
        while len(answer) < rows * cols:
            # Check step size
            if directions[direction_index] == "right" or directions[direction_index] == "left":
                step_size += 1
            
            # Check next direction
            if directions[direction_index] == "right":
                for j in range(curr_col + 1, curr_col + step_size + 1):
                    if perform_check(curr_row, j):
                        answer.append([curr_row, j])
                curr_col += step_size
            elif directions[direction_index] == "left":
                for j in range(curr_col - 1, curr_col - step_size - 1, -1):
                    if perform_check(curr_row, j):
                        answer.append([curr_row, j])
                curr_col -= step_size
            elif directions[direction_index] == "down":
                for i in range(curr_row + 1, curr_row + step_size + 1):
                    if perform_check(i, curr_col):
                        answer.append([i, curr_col])
                curr_row += step_size
            elif directions[direction_index] == "up":
                for i in range(curr_row - 1, curr_row - step_size - 1, -1):
                    if perform_check(i, curr_col):
                        answer.append([i, curr_col])
                curr_row -= step_size

            direction_index = (direction_index + 1) % 4
        return answer


