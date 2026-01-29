class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        num_rows = len(board)
        num_cols = len(board[0])
        def convert_to_coords(board_num):
            # Assume never get board_num = 0
            if (board_num // num_rows) % 2 == 0:
                # Must be going right
                if board_num % num_rows == 0:
                    return (num_rows - (board_num // num_rows), 0)
                return (num_rows - (board_num // num_rows) - 1, board_num % num_rows - 1)
            
            if board_num % num_rows == 0:
                return (num_rows - (board_num // num_rows), num_cols - 1)
            return (num_rows - (board_num // num_rows) - 1, num_cols - (board_num % num_rows))
        
        def convert_to_board(curr_row, curr_col):
            if num_rows % 2 == 0:
                if curr_row % 2 == 0:
                    return (num_rows - curr_row) * num_rows - curr_col
                
                return (num_rows - curr_row) * num_rows - (num_cols - curr_col - 1)
            
            if curr_row % 2 == 0:
                return (num_rows - curr_row) * num_rows - (num_cols - curr_col - 1)
                
            return (num_rows - curr_row) * num_rows - curr_col
        
        curr_queue = deque()
        curr_queue.append((0, num_rows - 1, 0))
        visited = set()
        while curr_queue:
            num_moves, curr_row, curr_col = curr_queue.popleft()
            if convert_to_board(curr_row, curr_col) == num_rows * num_cols:
                return num_moves
            
            if (curr_row, curr_col) in visited:
                continue
            visited.add((curr_row, curr_col))
            
            # If we visit a blank space further on, no point in checking earlier blank spaces
            found_blank = False
            for i in range(6, 0, -1):
                next_pos = min(convert_to_board(curr_row, curr_col) + i, num_rows * num_cols)
                next_row, next_col = convert_to_coords(next_pos)
                if board[next_row][next_col] == -1:
                    if found_blank or ((next_row, next_col) in visited):
                        continue
                    found_blank = True
                    curr_queue.append((num_moves + 1, next_row, next_col))
                else:
                    next_row, next_col = convert_to_coords(board[next_row][next_col])
                    if board[next_row][next_col] not in visited:
                        curr_queue.append((num_moves + 1, next_row, next_col))
            print(curr_queue)
            print(visited)
        return -1 