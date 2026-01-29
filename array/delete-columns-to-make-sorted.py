class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num_rows = len(strs)
        num_cols = len(strs[0])
        num_cols_to_delete = 0
        for j in range(num_cols):
            for i in range(1, num_rows):
                if strs[i - 1][j] > strs[i][j]:
                    num_cols_to_delete += 1
                    break
        return num_cols_to_delete
