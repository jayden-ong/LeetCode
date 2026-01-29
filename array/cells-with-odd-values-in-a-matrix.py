class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Number of cells affected in m + n - 2
        # Will store a row_dict
        row_dict = {}
        for i in range(m):
            row_dict[i] = 0
        
        col_dict = {}
        for j in range(n):
            col_dict[j] = 0
        
        for index in indices:
            row_dict[index[0]] += 1
            col_dict[index[1]] += 1
        
        answer = 0
        for i in range(m):
            for j in range(n):
                if (row_dict[i] + col_dict[j]) % 2 == 1:
                    answer += 1
        return answer