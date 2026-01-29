class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # x is upper left of y if:
        #     x1 < x2
        #     y1 > y2
        answer = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                
                if points[i][0] <= points[j][0] and points[i][1] >= points[j][1]:
                    valid = True
                    for k in range(len(points)):
                        if k == i or k == j:
                            continue
                        # Check upper left
                        if points[i][0] <= points[k][0] <= points[j][0] and points[i][1] >= points[k][1] >= points[j][1]:
                            valid = False
                            break
                    
                    if valid:
                        answer += 1
        return answer