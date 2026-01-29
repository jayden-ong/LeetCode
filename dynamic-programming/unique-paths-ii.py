class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        answer = []
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            new_row = [1] * n
            if i == 0:
                seen_obstacle = False
                for j in range(n):
                    if seen_obstacle or obstacleGrid[i][j] == 1:
                        new_row[j] = 0
                        seen_obstacle = True
            if i > 0:
                for j in range(n):
                    if obstacleGrid[i][j] == 1:
                        new_row[j] = 0
                    else:
                        if j == 0:
                            new_row[j] = answer[i - 1][j]
                        else:
                            new_row[j] = new_row[j - 1] + answer[i - 1][j]
            answer.append(new_row)
        return answer[-1][-1]