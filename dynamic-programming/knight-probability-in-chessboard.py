from collections import deque
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < n
        
        if k == 0:
            return 1
        
        dp = []
        num_moves = 0
        while num_moves < k:
            if num_moves == 0:
                for i in range(n):
                    new_row = []
                    for j in range(n):
                        num_inside = 0
                        for direction in directions:
                            new_row_val, new_col_val = i + direction[0], j + direction[1]
                            if is_valid(new_row_val, new_col_val):
                                num_inside += 1
                        new_row.append(num_inside / 8)
                    dp.append(new_row)
            else:
                new_dp = []
                for i in range(n):
                    new_row = []
                    for j in range(n):
                        curr_prob = 0
                        for direction in directions:
                            new_row_val, new_col_val = i + direction[0], j + direction[1]
                            if is_valid(new_row_val, new_col_val):
                                curr_prob += dp[new_row_val][new_col_val] / 8
                        new_row.append(curr_prob)
                    new_dp.append(new_row)
                dp = new_dp
            num_moves += 1
        return dp[row][column]