class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mod_matrix = []
        answer = []
        for i in range(n):
            mod_matrix.append([0] * n)
            answer.append([0] * n)
        answer[0][0] += 1

        for start_row, start_col, end_row, end_col in queries:
            for i in range(start_row, end_row + 1):
                mod_matrix[i][start_col] += 1
                if end_col < n - 1:
                    mod_matrix[i][end_col + 1] -= 1
        
        for i in range(n):
            curr = 0
            for j in range(n):
                curr += mod_matrix[i][j]
                answer[i][j] = curr
        return answer