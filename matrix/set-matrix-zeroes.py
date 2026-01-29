class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        rows_to_zero = set()
        cols_to_zero = set()
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)
        
        for row_num in rows_to_zero:
            for j in range(num_cols):
                matrix[row_num][j] = 0
        
        for col_num in cols_to_zero:
            for i in range(num_rows):
                matrix[i][col_num] = 0