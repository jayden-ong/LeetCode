class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        answer = 0
        for i in range(len(points) - 1):
            curr_largest_y = float('-inf')
            for j in range(i + 1, len(points)):
                if points[j][1] > points[i][1]:
                    continue
                
                if points[j][1] > curr_largest_y:
                    answer += 1
                curr_largest_y = max(curr_largest_y, points[j][1])
        return answer