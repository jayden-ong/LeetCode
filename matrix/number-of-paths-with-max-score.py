class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = pow(10, 9) + 7
        num_rows, num_cols = len(board), len(board[0])
        directions = [(0, -1), (-1, 0), (-1, -1)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < num_rows and 0 <= curr_col < num_cols
        
        visited = set()
        queue = deque()
        dp = [[[0, 0] for _ in range(num_cols)] for _ in range(num_rows)]
        dp[-1][-1][1] = 1
        print(dp)
        queue.append((num_rows - 1, num_cols - 1))
        while queue:
            curr_row, curr_col = queue.popleft()
            curr_state = dp[curr_row][curr_col]
            if curr_row != num_rows - 1 or curr_col != num_cols - 1:
                for add_row, add_col in directions:
                    prev_row, prev_col = curr_row - add_row, curr_col - add_col
                    if not is_valid(prev_row, prev_col):
                        continue
                    
                    prev_state = dp[prev_row][prev_col]
                    if curr_state[0] < prev_state[0]:
                        curr_state[0], curr_state[1] = prev_state[0], prev_state[1]
                    elif curr_state[0] == prev_state[0]:
                        curr_state[1] += prev_state[1]
                if curr_row != 0 or curr_col != 0:
                    curr_state[0] += int(board[curr_row][curr_col])
            if curr_row == 0 and curr_col == 0:
                break
            
            for add_row, add_col in directions:
                new_row, new_col = curr_row + add_row, curr_col + add_col
                if (new_row, new_col) not in visited and is_valid(new_row, new_col) and board[new_row][new_col] != 'X':
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
            
        return [dp[0][0][0] % MOD, dp[0][0][1]]