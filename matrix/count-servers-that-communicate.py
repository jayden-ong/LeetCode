class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        server_rows = [0] * len(grid)
        server_cols = [0] * len(grid[0])
        answer = 0
        for i in range(len(grid)):
            temp = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    server_rows[i] += 1
                    server_cols[j] += 1
            if server_rows[i] >= 2:
                answer += server_rows[i]

        for j in range(len(server_cols)):
            if server_cols[j] >= 2:
                num_coms = 0
                for i in range(len(server_rows)):
                    if grid[i][j] == 1 and server_rows[i] == 1:
                        num_coms += 1
                answer += num_coms
        return answer