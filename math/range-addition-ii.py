class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # Each op has to be at least 1
        min_row_op = m
        min_col_op = n
        for op in ops:
            min_row_op = min(min_row_op, op[0])
            min_col_op = min(min_col_op, op[1])
        return min_row_op * min_col_op
