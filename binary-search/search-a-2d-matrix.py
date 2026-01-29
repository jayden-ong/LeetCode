class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Want to binary search over the first column to figure out which row to start with
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        # Want to store all col vals in a list
        first_col = []
        for i in range(num_rows):
            first_col.append(matrix[i][0])
        
        left = 0
        right = num_rows - 1
        search_row = -1
        if num_rows > 1:
            while left <= right:
                mid = (left + right) // 2
                if first_col[mid] == target:
                    return True
                elif first_col[mid] < target:
                    search_row = mid
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            search_row = 0

        # print(search_row)
        # Want to binary search over the selected row to figure out which col to choose
        if search_row == -1:
            return False
        
        row_to_search = matrix[search_row]
        left = 0
        right = num_cols - 1
        if num_cols == 1:
            return row_to_search[0] == target
        
        while left <= right:
            mid = (left + right) // 2
            if row_to_search[mid] == target:
                return True
            elif row_to_search[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False