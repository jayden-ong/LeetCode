class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows_dict = {}
        cols_dict = {}
        for i in range(n):
            rows_dict[i + 1] = [float('inf'), float('-inf')]
            cols_dict[i + 1] = [float('inf'), float('-inf')]
        
        for row, col in buildings:
            rows_dict[row][0], rows_dict[row][1] = min(rows_dict[row][0], col), max(rows_dict[row][1], col)
            cols_dict[col][0], cols_dict[col][1] = min(cols_dict[col][0], row), max(cols_dict[col][1], row)
        
        answer = 0
        for row, col in buildings:
            if cols_dict[col][0] < row < cols_dict[col][1] and rows_dict[row][0] < col < rows_dict[row][1]:
                answer += 1
        return answer