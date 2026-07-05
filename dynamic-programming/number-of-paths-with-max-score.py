class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = pow(10, 9) + 7
        num_rows, num_cols = len(board), len(board[0])
        directions = [(0, -1), (-1, 0), (-1, -1)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < num_rows and 0 <= curr_col < num_cols
        
        queue = deque()
        dp = [[[0, 0]] * num_cols for _ in range(num_rows)]
        queue.append((num_rows - 1, num_cols - 1, 0))
        while queue:
            curr_row, curr_col, curr_score = queue.popleft()
            if curr_row == 0 and curr_col == 0:
                if curr_score > dp[0][0][0]:
                    dp[0][0] = [curr_score, 1]
                elif curr_score == dp[0][0][0]:
                    dp[0][0][1] += 1 
                continue
            
            for add_row, add_col in directions:
                new_row, new_col = add_row + curr_row, add_col + curr_col
                if is_valid(new_row, new_col) and board[new_row][new_col] != 'X':
                    if board[new_row][new_col] == 'E':
                        queue.append((new_row, new_col, curr_score))
                    else:
                        queue.append((new_row, new_col, curr_score + int(board[new_row][new_col])))
        return dp[0][0]