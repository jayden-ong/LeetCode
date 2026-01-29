class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = []
        col_dict = []
        square_dict = []
        for i in range(9):
            row_dict.append({"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0})
            col_dict.append({"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0})
            square_dict.append({"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0})
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    # Check each row
                    row_dict[i][board[i][j]] += 1
                    if row_dict[i][board[i][j]] > 1:
                        return False
                    
                    # Check each column
                    col_dict[j][board[i][j]] += 1
                    if col_dict[j][board[i][j]] > 1:
                        print("col")
                        return False
                    
                    # Check each square
                    if i < 3 and j < 3:
                        first_coord = 0
                    elif i < 3 and j < 6:
                        first_coord = 1
                    elif i < 3 and j < 9:
                        first_coord = 2
                    elif i < 6 and j < 3:
                        first_coord = 3
                    elif i < 6 and j < 6:
                        first_coord = 4
                    elif i < 6 and j < 9:
                        first_coord = 5
                    elif i < 9 and j < 3:
                        first_coord = 6
                    elif i < 9 and j < 6:
                        first_coord = 7
                    elif i < 9 and j < 9:
                        first_coord = 8
                    
                    square_dict[first_coord][board[i][j]] += 1
                    if square_dict[first_coord][board[i][j]] > 1:
                        print("square")
                        return False
                        
        return True