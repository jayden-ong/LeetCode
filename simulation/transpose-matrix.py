class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        curr_row = 0
        curr_col = 0

        answer = []
        for i in range(num_cols):
            curr = []
            for j in range(num_rows):
                curr.append(matrix[curr_row][curr_col])
                curr_row += 1
                if curr_row >= num_rows:
                    curr_row = 0
                    curr_col += 1
            answer.append(curr)
        return answer