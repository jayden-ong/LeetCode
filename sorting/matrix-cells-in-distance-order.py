from collections import deque
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cells_explored = {}
        curr_answer = []
        stack = deque()
        stack.append((rCenter, cCenter))
        while stack:
            curr_row, curr_col = stack.popleft()
            if (curr_row, curr_col) not in cells_explored:
                if curr_row > 0 and (curr_row - 1, curr_col) not in cells_explored:
                    stack.append((curr_row - 1, curr_col))
                
                if curr_row < rows - 1 and (curr_row + 1, curr_col) not in cells_explored:
                    stack.append((curr_row + 1, curr_col))
                
                if curr_col > 0 and (curr_row, curr_col - 1) not in cells_explored:
                    stack.append((curr_row, curr_col - 1))
                
                if curr_col < cols - 1 and (curr_row, curr_col + 1) not in cells_explored:
                    stack.append((curr_row, curr_col + 1))
                
                cells_explored[(curr_row, curr_col)] = True
                curr_answer.append([curr_row, curr_col])
                
        return curr_answer