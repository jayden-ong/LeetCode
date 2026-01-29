class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        num_rows = len(mat)
        num_cols = len(mat[0])
        k %= num_cols
        for i in range(num_rows):
            for j in range(num_cols):
                if i % 2 == 0:
                    replacement = (j + k) % num_cols
                else:
                    replacement = (j - k)
                if mat[i][j] != mat[i][replacement]:
                    return False
        return True