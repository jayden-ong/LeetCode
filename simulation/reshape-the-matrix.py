class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Check for validity
        num_rows = len(mat)
        num_cols = len(mat[0])
        if num_rows * num_cols != r * c:
            return mat
        
        curr_mat = []
        mat_i = 0
        mat_j = 0
        for i in range(r):
            curr_row = []
            for j in range(c):
                curr_row.append(mat[mat_i][mat_j])
                # If done correctly, mat_i should never exceed num_rows
                if mat_j == num_cols - 1:
                    mat_i += 1
                    mat_j = 0
                else:
                    mat_j += 1
            curr_mat.append(curr_row)
        return curr_mat