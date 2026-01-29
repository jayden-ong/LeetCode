class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        grid[0][0] = 0
        grid[1][-1] = 0
        top_row_sum = sum(grid[0])
        bottom_row_sum = 0
        answer = top_row_sum
        for i in range(1, len(grid[0])):
            top_row_sum -= grid[0][i]
            bottom_row_sum += grid[1][i - 1]
            curr_best = max(top_row_sum, bottom_row_sum)
            answer = min(answer, curr_best)
        return answer
        