class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        answer = 0
        def check_intersection(x11, x12, y11, y12, x21, x22, y21, y22):
            if x11 > x22 or y11 > y22 or x21 > x12 or y21 > y12:
                return False
            return True

        for i in range(len(bottomLeft) - 1):
            for j in range(i + 1, len(topRight)):
                # Check intersection
                if not check_intersection(bottomLeft[i][0], topRight[i][0], bottomLeft[i][1], topRight[i][1], bottomLeft[j][0], topRight[j][0], bottomLeft[j][1], topRight[j][1]):
                    continue
                
                left, right = max(bottomLeft[i][0], bottomLeft[j][0]), min(topRight[i][0], topRight[j][0])
                bottom, top = max(bottomLeft[i][1], bottomLeft[j][1]), min(topRight[i][1], topRight[j][1])
                answer = max(answer, min(right - left, top - bottom) ** 2)
        return answer