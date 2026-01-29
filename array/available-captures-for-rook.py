class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            if "R" in board[i]:
                rook_row = i
                rook_col = board[i].index("R")
                break
        
        # Go up
        num_captures = 0
        for i in range(rook_row - 1, -1, -1):
            # Rook cannot take
            if board[i][rook_col] == "B":
                break
            elif board[i][rook_col] == "p":
                num_captures += 1
                break
        
        for i in range(rook_row + 1, 8, 1):
            # Rook cannot take
            if board[i][rook_col] == "B":
                break
            elif board[i][rook_col] == "p":
                num_captures += 1
                break

        for i in range(rook_col - 1, -1, -1):
            if board[rook_row][i] == "B":
                break
            elif board[rook_row][i] == "p":
                num_captures += 1
                break
        
        for i in range(rook_col + 1, 8, 1):
            if board[rook_row][i] == "B":
                break
            elif board[rook_row][i] == "p":
                num_captures += 1
                break
        return num_captures