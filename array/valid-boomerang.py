from operator import add, sub
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # Need to find equation for the function
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        
        # Vertical line
        if points[1][0] - points[0][0] == 0:
            if points[2][0] == points[1][0]:
                return False
            return True
        
        coeff = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])

        y_intercept = points[0][1] - coeff * points[0][0]
        #print(coeff)
        #print(y_intercept)
        #print(coeff * points[2][0] + y_intercept)
        #print(points[2][1])
        if abs(coeff * points[2][0] + y_intercept - points[2][1]) < 0.00001:
            return False
        return True