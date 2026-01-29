from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        # If there is empty square with adjacent mine, stop recursion
        num_rows = len(board)
        num_cols = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        def is_valid(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols

        tiles_seen = set()
        stack = deque()
        stack.append(click)
        while stack:
            curr_row, curr_col = stack.popleft()
            # Want to add tiles to stack, only if curr tile is not adjacent to a bomb
            new_tiles = []
            bombs = 0
            for direction in directions:
                new_row, new_col = direction[0] + curr_row, direction[1] + curr_col
                if is_valid(new_row, new_col):
                    if board[new_row][new_col] == "M":
                        bombs += 1
                    
                    if board[new_row][new_col] == 'E':
                        new_tiles.append((new_row, new_col))
                
            if bombs == 0:
                for tile in new_tiles:
                    if tile not in tiles_seen:
                        stack.append(tile)
                    tiles_seen.add(tile)
                board[curr_row][curr_col] = "B"
            else:
                board[curr_row][curr_col] = str(bombs)
        return board
