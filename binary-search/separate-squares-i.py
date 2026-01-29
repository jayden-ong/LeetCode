class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        bottom_barrier = float('inf')
        top_barrier = float('-inf')
        area = 0
        for _, bottom, length in squares:
            bottom_barrier = min(bottom_barrier, bottom)
            top_barrier = max(top_barrier, bottom + length)
            area += pow(length, 2)
        
        def validate(y_line):
            curr_area = 0
            for _, bottom, length in squares:
                if bottom < y_line:
                    curr_area += length * min(y_line - bottom, length)
            return curr_area >= area / 2
        
        while abs(top_barrier - bottom_barrier) > pow(10, -5):
            mid = (top_barrier + bottom_barrier) / 2
            if validate(mid):
                top_barrier = mid
            else:
                bottom_barrier = mid
        return top_barrier
        