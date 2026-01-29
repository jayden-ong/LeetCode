class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Want to create a DP array for each position in the triangle
        # It will store the minimum sum of the path required to reach it
        dp = []
        for i in range(len(triangle)):
            if i == 0:
                dp.append([triangle[0][0]])
            else:
                curr_row = []
                for j in range(len(triangle[i])):
                    curr_best = float('inf')
                    # Can only look at index i and index i - 1
                    if j > 0:
                        curr_best = min(curr_best, dp[i - 1][j - 1])
                    
                    if j < len(triangle[i]) - 1:
                        curr_best = min(curr_best, dp[i - 1][j])
                    curr_row.append(curr_best + triangle[i][j])
                dp.append(curr_row)
        return min(dp[-1])