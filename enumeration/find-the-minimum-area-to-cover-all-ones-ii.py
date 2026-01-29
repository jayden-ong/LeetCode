class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        # bottom and right are exclusive
        def find_smallest_rectangle(grid, top, bottom, left, right):
            contains_one = False
            f_bottom, f_top = top, bottom
            f_left, f_right = right, left
            for i in range(top, bottom):
                for j in range(left, right):
                    if grid[i][j] == 1:
                        f_bottom = max(f_bottom, i)
                        f_top = min(f_top, i)
                        f_left = min(f_left, j)
                        f_right = max(f_right, j)
                        contains_one = True
            if not contains_one:
                return 0
            return (f_bottom - f_top + 1) * (f_right - f_left + 1)
        
        def rotate(grid):
            return [[grid[i][j] for i in range(len(grid) - 1, -1, -1)] for j in range(len(grid[0]))]

        answer = float('inf')
        for _ in range(4):
            for i in range(1, len(grid)):
                first_area = find_smallest_rectangle(grid, 0, i, 0, len(grid[0]))
                for j in range(1, len(grid[0])):
                    second_area = find_smallest_rectangle(grid, i, len(grid), 0, j)
                    third_area = find_smallest_rectangle(grid, i, len(grid), j, len(grid[0]))
                    answer = min(answer, first_area + second_area + third_area)
                for i2 in range(i + 1, len(grid)):
                    second_area = find_smallest_rectangle(grid, i, i2, 0, len(grid[0]))
                    third_area = find_smallest_rectangle(grid, i2, len(grid), 0, len(grid[0]))
                    answer = min(answer, first_area + second_area + third_area)
            grid = rotate(grid)
        return answer