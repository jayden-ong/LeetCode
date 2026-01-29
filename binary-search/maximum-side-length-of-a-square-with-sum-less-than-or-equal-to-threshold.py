class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        max_length = min(len(mat), len(mat[0]))
        prefix_sum = [[0] * len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            curr = 0
            for j in range(len(mat[0])):
                curr += mat[i][j]
                prefix_sum[i][j] = curr
        prefix_sum_col = [[0] * len(mat[0]) for _ in range(len(mat))]
        for j in range(len(mat[0])):
            curr = 0
            for i in range(len(mat)):
                curr += mat[i][j]
                prefix_sum_col[i][j] = curr
        
        # print(prefix_sum_col)
        # print(prefix_sum)
        def determine_sum(edge_length, curr_row, curr_col):
            curr = 0
            for i in range(curr_row, curr_row + edge_length):
                curr += prefix_sum[i][curr_col + edge_length - 1]
                if curr_col > 0:
                    curr -= prefix_sum[i][curr_col - 1]
            return curr

        for length in range(max_length, 0, -1):
            for i in range(len(mat) - length + 1):
                curr_sum = determine_sum(length, i, 0)
                for j in range(len(mat[0]) - length + 1):
                    if curr_sum <= threshold:
                        print(len(mat))
                        print(len(mat[0]))
                        print(i)
                        print(j)
                        return length
                    
                    if j != len(mat[0]) - length:
                        # Add next col
                        curr_sum += prefix_sum_col[i + length - 1][j + length]
                        # Remove prev col
                        curr_sum -= prefix_sum_col[i + length - 1][j]
                        if i > 0:
                            curr_sum -= prefix_sum_col[i - 1][j + length]
                            curr_sum += prefix_sum_col[i - 1][j]
                        
        return 0