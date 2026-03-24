class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        final = 1
        answer = []
        for i in range(len(grid)):
            new_row = []
            for j in range(len(grid[0])):
                final *= grid[i][j]
                new_row.append(1)
            answer.append(new_row)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                answer[i][j] = (final // grid[i][j]) % MOD
        return answer