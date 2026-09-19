class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        '''
        def check_overlap(x, y):
            return x1 <= x <= x2 and y1 <= y <= y2
        
        def check_within_circle(x, y):
            return ((x - xCenter) ** 2 + (y - yCenter) ** 2) ** 0.5 <= radius
        
        circle_points = [(xCenter + radius, yCenter), (xCenter - radius, yCenter), (xCenter, yCenter + radius), (xCenter, yCenter - radius)]
        for x, y in circle_points:
            if check_overlap(x, y):
                return True
        
        rectangle_points = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        for x, y in rectangle_points:
            if check_within_circle(x, y):
                return True
        return False
        '''
        if (x1 < (xCenter - radius) and x2 < (xCenter - radius)) or (x1 > (xCenter + radius) and x2 > (xCenter + radius)):
            return False
        
        if (y1 < (yCenter - radius) and y2 < (yCenter - radius)) or (y1 > (yCenter + radius) and y2 > (yCenter + radius)):
            return False
        return True