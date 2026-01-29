class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        answer = -1
        smallest_distance = 0
        i = 0
        for point in points:
            if point[0] == x or point[1] == y:
                if answer == -1:
                    answer = i
                    smallest_distance = abs(point[0] - x) + abs(point[1] - y)
                else:
                    if abs(point[0] - x) + abs(point[1] - y) < smallest_distance:
                        answer = i
                        smallest_distance = abs(point[0] - x) + abs(point[1] - y)

            i += 1
        return answer