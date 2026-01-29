class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Used to cut into rows
        rectangle_rows = []
        # Used to cut into cols
        rectangle_cols = []
        for start_x, start_y, end_x, end_y in rectangles:
            heapq.heappush(rectangle_cols, (start_x, end_x))
            heapq.heappush(rectangle_rows, (start_y, end_y))

        def divide(curr_heap):
            num_walls = 0
            while curr_heap and num_walls < 2:
                curr_top = heapq.heappop(curr_heap)[1]
                while curr_heap and curr_heap[0][0] < curr_top:
                    curr_top = max(curr_top, heapq.heappop(curr_heap)[1])
                if not curr_heap:
                    return False
                num_walls += 1
                print(num_walls)
            return num_walls == 2
        return divide(rectangle_rows) or divide(rectangle_cols)