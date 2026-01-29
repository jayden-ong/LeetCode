class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        directions = {(-1, 1) : (1, 1), (1, 1) : (1, -1), (1, -1) : (-1, -1), (-1, -1) : (-1, 1)}
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0])
        
        def find_v(curr_row, curr_col, direction_row, direction_col, length, length_left, desired_num, curr_answer):
            # (-1, -1) --> (-1, 1), (-1, 1) --> (-1, -1), (1, -1) --> (1, 1), (1, 1) --> (1, -1)
            # We can continue to go in this direction
            answer = length
            new_row, new_col = curr_row + direction_row, curr_col + direction_col
            if is_valid(new_row, new_col) and grid[new_row][new_col] == desired_num:
                # 1. We haven't turned yet -- keep going in this direction
                # 2. We have already turned -- the distance to go decreases by 1
                if length_left == -1:
                    answer = max(answer, find_v(new_row, new_col, direction_row, direction_col, length + 1, length_left, 2 - desired_num, curr_answer))
                else:
                    answer = max(answer, find_v(new_row, new_col, direction_row, direction_col, length, length_left + 1, 2 - desired_num, curr_answer))
            else:
                # We could end it here if we have already turned
                if length_left != -1:
                    return length + length_left
            
            # Could turn if we haven't already
            if length_left == -1:
                new_direction_row, new_direction_col = directions[(direction_row, direction_col)]
                new_row, new_col = curr_row + new_direction_row, curr_col + new_direction_col
                # Once we turn, we know our best possible answer and we can skip searching
                best_answer = length
                if (add_row, add_col) == (-1, 1):
                    best_answer += min(len(grid) - curr_row - 1, len(grid[0]) - curr_col - 1)
                elif (add_row, add_col) == (1, 1):
                    best_answer += min(len(grid) - curr_row - 1, curr_col)
                elif (add_row, add_col) == (1, -1):
                    best_answer += min(curr_row, curr_col)
                else:
                    best_answer += min(curr_row, len(grid[0]) - curr_col - 1)
                
                if is_valid(new_row, new_col) and grid[new_row][new_col] == desired_num and best_answer > curr_answer:
                    answer = max(answer, find_v(new_row, new_col, new_direction_row, new_direction_col, length, 1, 2 - desired_num, curr_answer))

            return answer

        def find_best(curr_row, curr_col, direction_row, direction_col):
            # 1. up, right
            # 2. down, right
            # 3. down, left
            # 4. up, left
            if (add_row, add_col) == (-1, 1):
                # Can only go right len(grid[0]) - 1 - curr_col many times
                # Can go up curr_row times
                return min(len(grid[0]) - curr_col, curr_row + len(grid))
            elif (add_row, add_col) == (1, 1):
                return min(len(grid[0]) - 1 + len(grid[0]) - curr_col, len(grid) - curr_row)
            elif (add_row, add_col) == (1, -1):
                return min(curr_col + 1, len(grid) - 1 + len(grid) - curr_row)
            return min(len(grid[0]) + curr_col, curr_row + 1)
        
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    answer = max(answer, 1)
                    for add_row, add_col in directions:
                        new_row, new_col = i + add_row, j + add_col
                        # Don't explore if we can't possibly do better?
                        if is_valid(new_row, new_col) and grid[new_row][new_col] == 2:
                            # Want to figure out the best possible answer to see if we can skip searching
                            if find_best(i, j, add_row, add_col) > answer:
                                answer = max(answer, find_v(new_row, new_col, add_row, add_col, 2, -1, 0, answer))
        return answer
