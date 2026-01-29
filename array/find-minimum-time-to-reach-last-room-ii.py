class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < len(moveTime) and 0 <= curr_col < len(moveTime[0])
        
        queue = [(0, 1, 0, 0)]
        visited = set()
        while queue:
            curr_time, curr_penalty, curr_row, curr_col = heapq.heappop(queue)
            if (curr_row, curr_col) in visited:
                continue
            visited.add((curr_row, curr_col))
            
            if curr_row == len(moveTime) - 1 and curr_col == len(moveTime[0]) - 1:
                return curr_time
            
            for add_row, add_col in directions:
                new_row, new_col = curr_row + add_row, curr_col + add_col
                if is_valid(new_row, new_col) and (new_row, new_col) not in visited:
                    heapq.heappush(queue, (max(curr_time, moveTime[new_row][new_col]) + curr_penalty, 3 - curr_penalty, new_row, new_col))
        # Should never run
        return -1
