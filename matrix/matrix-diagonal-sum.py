class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        num_rows = len(mat)
        num_cols = len(mat[0])
        j = num_cols - 1
        answer = 0
        for i in range(num_rows):
            answer += mat[i][i]
            if j != i:
                answer += mat[i][j]
            j -= 1
        return answer