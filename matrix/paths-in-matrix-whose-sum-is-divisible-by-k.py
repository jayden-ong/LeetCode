class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = pow(10, 9) + 7
        dp = [[[0 for l in range(k)] for j in range(len(grid[0]))] for i in range(len(grid))]
        dp[0][0][grid[0][0] % k] += 1
        # No chance of navigating the same path twice
        cell_queue = deque()
        cell_queue.append((0, 0))
        visited = set()
        visited.add((0, 0))
        while cell_queue:
            curr_row, curr_col = cell_queue.popleft()
            if curr_row + 1 != len(grid) and (curr_row + 1, curr_col) not in visited:
                cell_queue.append((curr_row + 1, curr_col))
                visited.add((curr_row + 1, curr_col))
            if curr_col + 1 != len(grid[0]) and (curr_row, curr_col + 1) not in visited:
                cell_queue.append((curr_row, curr_col + 1))
                visited.add((curr_row, curr_col + 1))
            
            visited.add((curr_row, curr_col))
            for value in range(k):
                if dp[curr_row][curr_col][value] > 0:
                    if curr_row + 1 != len(grid):
                        dp[curr_row + 1][curr_col][(value + grid[curr_row + 1][curr_col]) % k] += dp[curr_row][curr_col][value]
                        dp[curr_row + 1][curr_col][(value + grid[curr_row + 1][curr_col]) % k] %= MOD
                    if curr_col + 1 != len(grid[0]):
                        dp[curr_row][curr_col + 1][(value + grid[curr_row][curr_col + 1]) % k] += dp[curr_row][curr_col][value]
                        dp[curr_row][curr_col + 1][(value + grid[curr_row][curr_col + 1]) % k] %= MOD
        return dp[-1][-1][0]
        