class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        not_flip_set = set()
        num_rows = len(board)
        num_cols = len(board[0])

        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < num_rows and 0 <= curr_col < num_cols

        def bfs(curr_row, curr_col):
            curr_stack = [(curr_row, curr_col)]
            already_explored = set()
            while curr_stack:
                i, j = curr_stack.pop()
                not_flip_set.add((i, j))
                already_explored.add((i, j))
                for direction in directions:
                    new_i, new_j = i + direction[0], j + direction[1]
                    if is_valid(new_i, new_j) and board[new_i][new_j] == "O" and (new_i, new_j) not in already_explored:
                        curr_stack.append((new_i, new_j))

        # Need to check all boundaries (top and bottom row)
        for j in range(num_cols):
            if board[0][j] == "O" and (0, j) not in not_flip_set:
                bfs(0, j)
            
            if board[num_rows - 1][j] == "O" and (num_rows - 1, j) not in not_flip_set:
                bfs(num_rows - 1, j)
        
        # Need to check all boundaries(left and right)
        for i in range(num_rows):
            if board[i][0] == "O" and (i, 0) not in not_flip_set:
                bfs(i, 0)
            
            if board[i][num_cols - 1] == "O" and (i, num_cols - 1) not in not_flip_set:
                bfs(i, num_cols - 1)
        # If the coords are not in the non-flip-set, have to flip
        # print(not_flip_set)
        for i in range(num_rows):
            for j in range(num_cols):
                if (i, j) not in not_flip_set:
                    board[i][j] = "X"
