class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        answer = float('inf')
        for start, end, distance in roads:
            answer = min(answer, distance)
        return answer