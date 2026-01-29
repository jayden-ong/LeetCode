class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        cols_list = []
        # Each will store the length of the set and the numbers seen
        for i in range(0, num_rows):
            cols_list.append([0, set()])
        
        for i in range(num_rows):
            curr_row_nums = set()
            num_nums = 0
            for j in range(num_cols):
                # For the row
                if matrix[i][j] not in curr_row_nums:
                    curr_row_nums.add(matrix[i][j])
                    num_nums += 1
                
                # For the col
                if matrix[i][j] not in cols_list[j][1]:
                    cols_list[j][1].add(matrix[i][j])
                    cols_list[j][0] += 1
            
            if num_nums != num_rows:
                return False
        
        for pair in cols_list:
            if pair[0] != num_rows:
                return False
        return True