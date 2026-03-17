class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        mod_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        answer = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr_val = 0
                if matrix[i][j] == 1:
                    if i > 0:
                        curr_val += mod_matrix[i - 1][j]
                    curr_val += matrix[i][j]
                mod_matrix[i][j] = curr_val
            
            curr_row = sorted(mod_matrix[i], reverse=True)
            for j in range(len(matrix[0])):
                answer = max(answer, curr_row[j] * (j + 1))
        
        return answer