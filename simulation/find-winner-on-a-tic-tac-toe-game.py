class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        num_moves = len(moves)
        board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        for i in range(num_moves):
            symbol = 'O'
            if i % 2 == 0:
                symbol = 'X'
            
            board[moves[i][0]][moves[i][1]] = symbol
        
        # Check rows
        for i in range(3):
            if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X':
                return "A"
            elif board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O':
                return "B"
        # Check rows
        for i in range(3):
            if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
                return "A"
            elif board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
                return "B"
        
        # Check diagonals
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
            return "A"
        elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            return "B"
        
        if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
            return "A"
        elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
            return "B"

        if num_moves == 9:
            return "Draw"
        return "Pending"