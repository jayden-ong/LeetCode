class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < len(moveTime) and 0 <= curr_col < len(moveTime[0])
        
        curr_queue = [(0, 0, 0)]
        explored = set()
        while curr_queue:
            curr_time, curr_row, curr_col = heapq.heappop(curr_queue)
            if curr_row == len(moveTime) - 1 and curr_col == len(moveTime[0]) - 1:
                return curr_time
            
            if (curr_row, curr_col) in explored:
                continue
            explored.add((curr_row, curr_col))
        
            for add_row, add_col in directions:
                new_row, new_col = add_row + curr_row, add_col + curr_col
                if is_valid(new_row, new_col) and (new_row, new_col) not in explored:
                    heapq.heappush(curr_queue, (max(curr_time, moveTime[new_row][new_col]) + 1, new_row, new_col))
            
        # Should never run
        return -1