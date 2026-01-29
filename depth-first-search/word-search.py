from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Find all instances of the first letter and check surrounding area
        # If it is there, keep going and make sure that new coordinates are
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        num_rows = len(board)
        num_cols = len(board[0])
        length_word = len(word)

        def is_valid(curr_row, curr_col):
            return curr_row >= 0 and curr_row < num_rows and curr_col >= 0 and curr_col < num_cols
        # not part of old coordinates

        for char in word:
            found = False
            for i in range(num_rows):
                if char in board[i]:
                    found = True
                    break
            
            if not found:
                return False
        
        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] == word[0]:
                    # Each item stores the current index, and current coords used
                    stack = deque()
                    coords_set = set()
                    coords_set.add((i, j))
                    stack.append((1, coords_set, i, j))
                    while stack:
                        curr_index, curr_coords_set, row, col = stack.popleft()
                        if curr_index == length_word:
                            return True

                        for direction in directions:
                            curr_row, curr_col = row + direction[0], col + direction[1]
                            set_copy = curr_coords_set.copy()
                            if is_valid(curr_row, curr_col) and board[curr_row][curr_col] == word[curr_index] and (curr_row, curr_col) not in curr_coords_set:
                                set_copy.add((curr_row, curr_col))
                                stack.append((curr_index + 1, set_copy, curr_row, curr_col))
        return False
                                