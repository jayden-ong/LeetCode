class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n = len(grid)
        c = len(grid[0])
        num_cols = c
        answer = 0
        while num_cols > 0:
            curr_greatest = float('-inf')
            for i in range(n):
                row_greatest = grid[i][0]
                index_greatest = 0
                for j in range(1, c):
                    if grid[i][j] > row_greatest:
                        row_greatest = grid[i][j]
                        index_greatest = j
                grid[i][index_greatest] = float('-inf')
                curr_greatest = max(curr_greatest, row_greatest)
            answer += curr_greatest
            num_cols -= 1
        return answer