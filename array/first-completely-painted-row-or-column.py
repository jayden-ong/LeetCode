class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Want to map each number to its row and column numbers
        numbers_dict = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                numbers_dict[mat[i][j]] = (i, j)
        
        rows_remaining = [len(mat[0])] * len(mat)
        cols_remaining = [len(mat)] * len(mat[0])
        for i, paint_num in enumerate(arr):
            curr_row, curr_col = numbers_dict[paint_num]
            rows_remaining[curr_row] -= 1
            if rows_remaining[curr_row] == 0:
                return i
            
            cols_remaining[curr_col] -= 1
            if cols_remaining[curr_col] == 0:
                return i
        
        # should never run
        return -1