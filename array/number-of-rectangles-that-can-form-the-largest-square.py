class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        curr_largest = min(rectangles[0][0], rectangles[0][1])
        answer = 1
        num_rectangles = len(rectangles)
        for i in range(1, num_rectangles):
            if min(rectangles[i][0], rectangles[i][1]) > curr_largest:
                curr_largest = min(rectangles[i][0], rectangles[i][1])
                answer = 1
            elif min(rectangles[i][0], rectangles[i][1]) == curr_largest:
                answer += 1
        return answer