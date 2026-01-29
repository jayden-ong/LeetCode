class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        num_x = 0
        num_o = 0
        for row in board:
            for char in row:
                if char == "X":
                    num_x += 1
                elif char == "O":
                    num_o += 1
        
        if num_o > num_x or num_x > num_o + 1:
            return False
        
        # Need to check if anyone has one
        num_x_wins = 0
        num_o_wins = 0
        for row in board:
            if row == "XXX":
                num_x_wins += 1
            elif row == "OOO":
                num_o_wins += 1
        
        for i in range(len(board[0])):
            if board[0][i] + board[1][i] + board[2][i] == "XXX":
                num_x_wins += 1
            elif board[0][i] + board[1][i] + board[2][i] == "OOO":
                num_o_wins += 1
        
        if board[0][0] + board[1][1] + board[2][2] == "XXX":
            num_x_wins += 1
        elif board[0][0] + board[1][1] + board[2][2] == "OOO":
            num_o_wins += 1
        
        if board[0][2] + board[1][1] + board[2][0] == "XXX":
            num_x_wins += 1
        elif board[0][2] + board[1][1] + board[2][0] == "OOO":
            num_o_wins += 1
        
        if num_x_wins > 0 and num_o_wins > 0:
            return False
        
        if num_x_wins > 0 and num_o >= num_x:
            return False
        
        if num_o_wins > 0 and num_x > num_o:
            return False
        
        return True