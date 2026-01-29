class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        # Can only teleport somewhere with a smaller or equal cost
        coords = []
        min_costs = []
        for i in range(len(grid)):
            new_row = []
            for j in range(len(grid[0])):
                coords.append((i, j))
                new_row.append(float('inf'))
            min_costs.append(new_row)
        coords.sort(key=lambda x: grid[x[0]][x[1]])
        for _ in range(k + 1):
            min_cost = float('inf')
            j = 0
            for i in range(len(coords)):
                min_cost = min(min_cost, min_costs[coords[i][0]][coords[i][1]])
                # If the next coord has the same value, skip it -- will be dealt with when we get to last one
                if i + 1 < len(coords) and grid[coords[i][0]][coords[i][1]] == grid[coords[i + 1][0]][coords[i + 1][1]]:
                    # i += 1
                    continue

                # Go over all previous points since we can teleport from this point to all previous points
                for x in range(j, i + 1):
                    min_costs[coords[x][0]][coords[x][1]] = min_cost
                j = i + 1
            
            for i in range(len(grid) - 1, -1, -1):
                for j in range(len(grid[0]) - 1, -1, -1):
                    if i == len(grid) - 1 and j == len(grid[0]) - 1:
                        min_costs[i][j] = 0
                        continue
                    if i != len(grid) - 1:
                        min_costs[i][j] = min(min_costs[i][j], min_costs[i + 1][j] + grid[i + 1][j])
                    if j != len(grid[0]) - 1:
                        min_costs[i][j] = min(min_costs[i][j], min_costs[i][j + 1] + grid[i][j + 1])
                    
        return min_costs[0][0]
