class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        priority_queue = []
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0])
        directions_dict = {1 : (0, 1), 2 : (0, -1), 3 : (1, 0), 4 : (-1, 0)}
        
        # cost, row, column
        tiles_explored = set()
        heapq.heappush(priority_queue, (0, 0, 0))
        while priority_queue:
            curr_cost, curr_row, curr_col = heapq.heappop(priority_queue)
            if (curr_row, curr_col) not in tiles_explored:
                if curr_row == len(grid) - 1 and curr_col == len(grid[0]) - 1:
                    return curr_cost
                
                tiles_explored.add((curr_row, curr_col))
                for i in range(1, 5):
                    cost = 1
                    if i == grid[curr_row][curr_col]:
                        cost = 0
                    
                    new_row, new_col = curr_row + directions_dict[i][0], curr_col + directions_dict[i][1]
                    if is_valid(new_row, new_col) and (new_row, new_col) not in tiles_explored:
                        heapq.heappush(priority_queue, (cost + curr_cost, new_row, new_col))

        # should never run
        return -1