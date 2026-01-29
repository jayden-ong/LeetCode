class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        num_coordinates = len(coordinates)
        if num_coordinates <= 2:
            return True
        
        # Want to get equation of the line
        coordinate1 = coordinates[0]
        coordinate2 = coordinates[1]
        if coordinate2[0] != coordinate1[0]:
            slope = (coordinate2[1] - coordinate1[1]) / (coordinate2[0] - coordinate1[0])
            y_intercept = coordinate1[1] - slope * coordinate1[0]
            for i in range(2, num_coordinates):
                curr_point = coordinates[i]
                if abs((slope * curr_point[0] + y_intercept) - curr_point[1]) >= 0.00001:
                    return False
            return True
        else:
            for i in range(2, num_coordinates):
                curr_point = coordinates[i]
                if curr_point[0] != coordinate1[0]:
                    return False
            return True
        