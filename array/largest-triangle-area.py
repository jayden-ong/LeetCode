class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = -1
        num_points = len(points)
        for i in range(num_points - 2):
            for j in range(i + 1, num_points - 1):
                for k in range(j + 1, num_points):
                    max_area = max(max_area, 0.5 * abs(points[i][0] * (points[j][1] - points[k][1]) + points[j][0] * (points[k][1] - points[i][1]) + points[k][0] * (points[i][1] - points[j][1])))
        return max_area