from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])
        answer = []
        for i in range(num_rows):
            answer.append([float('inf')] * num_cols)

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def is_valid(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols
        
        stack = deque()
        coords_explored = set()
        for i in range(num_rows):
            for j in range(num_cols):
                if mat[i][j] == 0:
                    stack.append((0, i, j))
                    answer[i][j] = 0
                    coords_explored.add((i, j))
        
        while stack:
            curr_distance, curr_row, curr_col = stack.popleft()
            for direction in directions:
                new_row, new_col = direction[0] + curr_row, direction[1] + curr_col
                if is_valid(new_row, new_col) and (new_row, new_col) not in coords_explored:
                    answer[new_row][new_col] = curr_distance + 1
                    stack.append((curr_distance + 1, new_row, new_col))
                    coords_explored.add((new_row, new_col))

        return answer
        