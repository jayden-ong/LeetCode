class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        rectangle_strips = []
        for x, y, l in squares:
            rectangle_strips.append((y, 1, x, x + l))
            rectangle_strips.append((y + l, -1, x, x + l))
        rectangle_strips.sort()

        def get_union_length(intervals):
            intervals.sort()
            answer, curr = 0, 0
            end = -10 ** 30
            for a, b in intervals:
                if a > end:
                    answer += b - a
                    end = b
                elif b > end:
                    answer += b - end
                    end = b
            return answer

        prev_y = rectangle_strips[0][0]
        area = 0
        areas = []
        x_ranges = []
        for y, event, x1, x2 in rectangle_strips:
            if y > prev_y and x_ranges:
                height = y - prev_y
                width = get_union_length(x_ranges)
                areas.append((prev_y, height, width))
                area += height * width
            if event == 1:
                x_ranges.append((x1, x2))
            else:
                x_ranges.remove((x1, x2))
            prev_y = y
        
        curr_area = 0
        half_area = area / 2
        for y, height, width in areas:
            if curr_area + height * width >= half_area:
                return y + (half_area - curr_area) / width
            curr_area += height * width
        return 0.0