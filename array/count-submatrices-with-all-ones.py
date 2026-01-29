class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        dp = [[0] * len(mat[0]) for _ in range(len(mat))]
        answer = 0
        for i, row in enumerate(mat):
            curr_row = []
            for j, num in enumerate(row):
                if j == 0:
                    dp[i][j] = mat[i][j]
                else:
                    if mat[i][j] == 0:
                        dp[i][j] == 0
                    else:
                        dp[i][j] = dp[i][j - 1] + 1
                
                curr = dp[i][j]
                for k in range(i, -1, -1):
                    curr = min(curr, dp[k][j])
                    if curr == 0:
                        break
                    answer += curr
            dp.append(curr_row)
        print(dp)
        return answer