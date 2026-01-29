class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Want to determine the tallest wall in each row
        num_rows = len(heightMap)
        num_cols = len(heightMap[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < num_rows and 0 <= curr_col < num_cols
        
        curr_cells = []
        for i in range(num_rows):
            heapq.heappush(curr_cells, (heightMap[i][0], i, 0))
            heapq.heappush(curr_cells, (heightMap[i][-1], i, num_cols - 1))
            heightMap[i][0] = -1
            heightMap[i][-1] = -1
        
        for j in range(num_cols):
            heapq.heappush(curr_cells, (heightMap[0][j], 0, j))
            heapq.heappush(curr_cells, (heightMap[-1][j], num_rows - 1, j))
            heightMap[0][j] = -1
            heightMap[-1][j] = -1
        
        answer = 0
        curr_level = 0
        while curr_cells:
            curr_height, curr_row, curr_col = heapq.heappop(curr_cells)
            curr_level = max(curr_level, curr_height)
            # Want to look at all adjacent tiles as their max water is curr_level - height
            for i in range(4):
                new_row, new_col = curr_row + directions[i][0], curr_col + directions[i][1]
                if is_valid(new_row, new_col) and heightMap[new_row][new_col] != -1:
                    curr = heightMap[new_row][new_col]
                    if curr < curr_level:
                        answer += curr_level - heightMap[new_row][new_col]
                    
                    heightMap[new_row][new_col] = -1
                    heapq.heappush(curr_cells, (curr, new_row, new_col))
        return answer
                    