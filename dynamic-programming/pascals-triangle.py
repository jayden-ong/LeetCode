class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        curr_triangle = []
        if numRows >= 1:
            curr_triangle.append([1])
        if numRows >= 2:
            curr_triangle.append([1,1])
        if numRows >= 3:
            for i in range(3, numRows + 1):
                curr_row = [1]
                prev_row = curr_triangle[-1]
                for j in range(len(prev_row) - 1):
                    curr_row.append(prev_row[j] + prev_row[j + 1])
                curr_row.append(1)
                curr_triangle.append(curr_row)
        return curr_triangle