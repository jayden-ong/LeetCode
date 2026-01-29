class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def flip_parity(row):
            new_row = []
            for num in row:
                if num == 0:
                    new_row.append(1)
                else:
                    new_row.append(0)
            return tuple(new_row)
        
        answer = 1
        rows_dict = defaultdict(int)
        num_rows = len(matrix)
        for row in matrix:
            if row[0] == 1:
                row = flip_parity(row)
            else:
                row = tuple(row)
            
            rows_dict[row] += 1
            answer = max(answer, rows_dict[row])
        return answer

