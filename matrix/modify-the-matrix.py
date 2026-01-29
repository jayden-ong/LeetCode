class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        answer = []
        curr_row = []
        for i in range(len(matrix)):
            answer.append(curr_row.copy())
        
        for j in range(len(matrix[0])):
            curr_max = 0
            coords_to_change = []
            for i in range(len(matrix)):
                answer[i].append(matrix[i][j])
                curr_max = max(curr_max, matrix[i][j])
                if matrix[i][j] == -1:
                    coords_to_change.append((i, j))
            
            for coord in coords_to_change:
                answer[coord[0]][coord[1]] = curr_max
        return answer