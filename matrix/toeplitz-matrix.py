class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        for i in range(num_cols):
            curr_row = 0
            curr_col = i
            curr_val = matrix[curr_row][curr_col]
            while curr_row < num_rows and curr_col < num_cols:
                if matrix[curr_row][curr_col] != curr_val:
                    return False
                curr_row += 1
                curr_col += 1
        
        for i in range(num_rows):
            curr_row = i
            curr_col = 0
            curr_val = matrix[curr_row][curr_col]
            while curr_row < num_rows and curr_col < num_cols:
                if matrix[curr_row][curr_col] != curr_val:
                    return False
                curr_row += 1
                curr_col += 1
        
        return True