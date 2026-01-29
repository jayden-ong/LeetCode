from operator import itemgetter
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key = itemgetter(0))
        num_points = len(points)
        answer = float('-inf')
        for i in range(1, num_points):
            answer = max(answer, points[i][0] - points[i - 1][0])
        return answer