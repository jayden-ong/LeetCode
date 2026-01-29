class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        num_elements = len(matrix) * len(matrix[0])
        # Want a variable that represents the limit
        left_wall = 0
        right_wall = num_cols - 1
        top_wall = 0
        bottom_wall = num_rows - 1
        while num_elements > 0:
            # Going right
            for i in range(left_wall, right_wall + 1):
                answer.append(matrix[top_wall][i])
                num_elements -= 1
            
            if num_elements <= 0:
                break
            top_wall += 1

            #print(answer)
            # Going down
            for j in range(top_wall, bottom_wall + 1):
                answer.append(matrix[j][right_wall])
                num_elements -= 1
            
            if num_elements <= 0:
                break
            right_wall -= 1
            
            #print(answer)
            # Going left
            for i in range(right_wall, left_wall - 1, -1):
                answer.append(matrix[bottom_wall][i])
                num_elements -= 1
            
            if num_elements <= 0:
                break
            bottom_wall -= 1

            #print(answer)
            # Going up
            for j in range(bottom_wall, top_wall - 1, -1):
                answer.append(matrix[j][left_wall])
                num_elements -= 1
            
            #print(answer)
            left_wall += 1
        return answer

