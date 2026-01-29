class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        num_rows = len(grid)
        answer = []
        for i in range(num_rows - 2):
            answer_row = []
            for j in range(num_rows - 2):
                new_row = grid[i][j:j + 3] + grid[i + 1][j:j + 3] + grid[i + 2][j:j + 3]
                answer_row.append(max(new_row))
            answer.append(answer_row)
        return answer