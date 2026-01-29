class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        dp = {}
        def solve(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i + 2 > j:
                return 0
            elif i + 2 == j:
                return values[i] * values[j] * values[i + 1]
            
            answer = float('inf')
            for k in range(i + 1, j):
                answer = min(answer, values[i] * values[j] * values[k] + solve(i, k) + solve(k, j))
            dp[(i, j)] = answer
            return answer
        return solve(0, len(values) - 1) 