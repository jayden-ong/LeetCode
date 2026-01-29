class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row_num = 0
        col_num = 0
        up = True
        answer = []
        while row_num != len(mat) - 1 or col_num != len(mat[0]) - 1:
            if up:
                while row_num >= 0 and col_num < len(mat[0]):
                    answer.append(mat[row_num][col_num])
                    row_num, col_num = row_num - 1, col_num + 1
                
                # Want to figure out where we left off
                # We go right as far as we can, then down
                row_num, col_num = row_num + 1, col_num - 1
                if col_num == len(mat[0]) - 1:
                    row_num += 1
                else:
                    col_num += 1
                up = False
            else:
                while row_num < len(mat) and col_num >= 0:
                    answer.append(mat[row_num][col_num])
                    row_num, col_num = row_num + 1, col_num - 1
                
                row_num, col_num = row_num - 1, col_num + 1
                if row_num == len(mat) - 1:
                    col_num += 1
                else:
                    row_num += 1
                up = True
        
        answer.append(mat[-1][-1])
        return answer