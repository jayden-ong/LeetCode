class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        num_rows = len(isWater)
        num_cols = len(isWater[0])
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < num_rows and 0 <= curr_col < num_cols

        # Any cell next to water has to be height 1
        answer = []
        # Contains all cells with heights already set
        cells_set = set()
        # Contains all cells that need to be explored
        pq = []
        for i in range(num_rows):
            curr_row = []
            for j in range(num_cols):
                if isWater[i][j] == 1:
                    cells_set.add((i, j))
                    heapq.heappush(pq, (0, i, j))
                curr_row.append(0)
            answer.append(curr_row)
        
        while len(cells_set) < num_rows * num_cols:
            curr_height, curr_row, curr_col = heapq.heappop(pq)
            for add_i, add_j in directions:
                new_i, new_j = curr_row + add_i, curr_col + add_j
                if is_valid(new_i, new_j) and (new_i, new_j) not in cells_set:
                    heapq.heappush(pq, (curr_height + 1, new_i, new_j))
                    answer[new_i][new_j] = curr_height + 1
                    cells_set.add((new_i, new_j))
        return answer
