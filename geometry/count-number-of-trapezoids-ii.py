class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        slope_to_intercept = defaultdict(list)
        midpoint_to_slope = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x2 == x1:
                    slope = float('inf')
                    intercept = x1
                else:
                    slope = (y2 - y1) / (x2 - x1)
                    intercept = (y1 * (x2 - x1) - x1 * (y2 - y1)) / (x2 - x1)
                
                midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
                slope_to_intercept[slope].append(intercept)
                midpoint_to_slope[midpoint].append(slope)
        
        answer = 0
        for slope_intercept_list in slope_to_intercept.values():
            # There are not enough common slopes
            if len(slope_intercept_list) == 1:
                continue

            intercept_to_count = defaultdict(int)
            for intercept in slope_intercept_list:
                intercept_to_count[intercept] += 1
            
            num_lines = 0
            # All of these lines have the same slope
            # We are just pairing them with other pairs that have different intercepts
            for count in intercept_to_count.values():
                answer += (num_lines * count)
                num_lines += count
            
        for midpoint_to_slope_list in midpoint_to_slope.values():
            if len(midpoint_to_slope_list) == 1:
                continue
                
            slope_to_count = defaultdict(int)
            for slope in midpoint_to_slope_list:
                slope_to_count[slope] += 1
                
            num_lines = 0
            # Get rid of all parallelograms
            for count in slope_to_count.values():
                answer -= num_lines * count
                num_lines += count
        return answer