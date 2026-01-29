class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        # Will store tuples
        min_in_rows = []
        # Will store single values
        max_in_cols = [0] * num_cols 
        # Want to get the min of rows and max of columns
        for i in range(num_rows):
            curr_smallest = 0
            curr_index = 0
            for j in range(num_cols):
                max_in_cols[j] = max(max_in_cols[j], matrix[i][j])
                if curr_smallest == 0 or matrix[i][j] < curr_smallest:
                    curr_smallest = matrix[i][j]
                    curr_index = j
            min_in_rows.append([curr_index, curr_smallest])
        
        answer = []
        #print(min_in_rows)
        #print(max_in_cols)
        for row_pair in min_in_rows:
            if row_pair[1] == max_in_cols[row_pair[0]]:
                answer.append(row_pair[1])
        return answer