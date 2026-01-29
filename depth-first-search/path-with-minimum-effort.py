class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        num_rows, num_cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def is_valid(row, col):
            return row >= 0 and row < num_rows and col >= 0 and col < num_cols
        
        least_possible_effort = []
        for _ in range(num_rows):
            least_possible_effort.append([float('inf')] * num_cols)
        least_possible_effort[0][0] = 0

        # First element is highest effort
        priority_queue = [(0, 0, 0)]
        while priority_queue:
            curr_effort, curr_row, curr_col = heapq.heappop(priority_queue)
            if curr_row == num_rows - 1 and curr_col == num_cols - 1:
                return curr_effort
            
            for direction in directions:
                new_row, new_col = curr_row + direction[0], curr_col + direction[1]
                if is_valid(new_row, new_col):
                    new_effort = max(curr_effort, abs(heights[curr_row][curr_col] - heights[new_row][new_col]))
                    if least_possible_effort[new_row][new_col] > new_effort:
                        heapq.heappush(priority_queue, (new_effort, new_row, new_col))
                        least_possible_effort[new_row][new_col] = new_effort
        return -1
        