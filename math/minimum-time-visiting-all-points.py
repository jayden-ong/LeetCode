class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        curr_location = points[0]
        num_points = len(points)
        curr_time = 0
        for i in range(1, num_points):
            curr_destination = points[i]

            x_diff = abs(curr_location[0] - curr_destination[0])
            y_diff = abs(curr_location[1] - curr_destination[1])

            if x_diff == y_diff:
                curr_location = curr_destination
                curr_time += x_diff
            elif x_diff < y_diff:
                curr_location[0] = curr_destination[0]
                curr_time += x_diff
                if curr_location[1] < curr_destination[1]:
                    curr_location[1] += x_diff
                else:
                    curr_location[1] -= x_diff
                curr_time += abs(curr_location[1] - curr_destination[1])
                curr_location[1] = curr_destination[1]
            else:
                curr_location[1] = curr_destination[1]
                curr_time += y_diff
                if curr_location[0] < curr_destination[0]:
                    curr_location[0] += y_diff
                else:
                    curr_location[0] -= y_diff
                curr_time += abs(curr_location[0] - curr_destination[0])
                curr_location[0] = curr_destination[0]
        return curr_time