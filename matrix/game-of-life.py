class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp_board = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < len(board) and 0 <= curr_col < len(board[0])
        
        for i in range(len(board)):
            curr_row = []
            for j in range(len(board[0])):
                num_live = 0
                for direction in directions:
                    new_row, new_col = i + direction[0], j + direction[1]
                    if is_valid(new_row, new_col):
                        if board[new_row][new_col] == 1:
                            num_live += 1

                if board[i][j] == 0:
                    if num_live == 3:
                        curr_row.append(1)
                    else:
                        curr_row.append(0)
                else:
                    if num_live < 2 or num_live > 3:
                        curr_row.append(0)
                    else:
                        curr_row.append(1)
            temp_board.append(curr_row)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = temp_board[i][j]