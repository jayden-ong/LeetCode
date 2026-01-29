class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        connections_dict = defaultdict(list)
        for first, second in connections:
            connections_dict[first].append(second)
            connections_dict[second].append(first)
        
        # Want to figure out which power grid each node belongs to
        node_to_grid = {}
        def build_power_grid(curr_node, visited, curr_grid, grid_number):
            # Add current node to the current grid
            curr_grid.append(curr_node)
            visited.add(curr_node)
            node_to_grid[curr_node] = grid_number
            for new_node in connections_dict[curr_node]:
                if new_node not in visited:
                    build_power_grid(new_node, visited, curr_grid, grid_number)
            return curr_grid

        visited = set()
        power_grids = []
        curr_grid_num = 0
        for i in range(1, c + 1):
            curr_grid = []
            if i not in visited:
                build_power_grid(i, visited, curr_grid, curr_grid_num)
                heapq.heapify(curr_grid)
                power_grids.append(curr_grid)
                curr_grid_num += 1
        
        # A station cannot come back online apparently
        invalid_stations = set()
        answer = []
        for order, station in queries:
            if order == 1:
                if station not in invalid_stations:
                    answer.append(station)
                else:
                    grid_num = node_to_grid[station]
                    power_grid = power_grids[grid_num]
                    while power_grid and power_grid[0] in invalid_stations:
                        heapq.heappop(power_grid)
                    if not power_grid:
                        answer.append(-1)
                    else:
                        answer.append(power_grid[0])
            else:
                invalid_stations.add(station)
        return answer
