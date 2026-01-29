class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        answer = []
        num_rows = len(grid)
        num_cols = len(grid[0])

        for j in range(num_cols):
            curr_widest = 0
            for i in range(num_rows):
                curr_widest = max(curr_widest, len(str(grid[i][j])))
            answer.append(curr_widest)
        return answer