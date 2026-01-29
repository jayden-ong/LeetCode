class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        temp_answer = []
        for row in box:
            new_row = ['.'] * len(row)
            num_stones = 0
            for i in range(len(row)):
                obj = row[i]
                if obj == "#":
                    num_stones += 1
                elif obj == "*":
                    new_row[i] = obj
                    if num_stones > 0:
                        for j in range(i - 1, max(-1, i - num_stones - 1), -1):
                            new_row[j] = "#"
                    num_stones = 0
            
            if num_stones > 0:
                for j in range(len(row) - 1, max(-1, len(row) - num_stones - 1), -1):
                    new_row[j] = "#"
            temp_answer.append(new_row)
        
        def flip_matrix(matrix):
            answer = []
            for i in range(len(matrix[0])):
                new_row = []
                for j in range(len(matrix) - 1, -1, -1):
                    new_row.append(matrix[j][i])
                answer.append(new_row)
            return answer
        # print(temp_answer)
        return flip_matrix(temp_answer)