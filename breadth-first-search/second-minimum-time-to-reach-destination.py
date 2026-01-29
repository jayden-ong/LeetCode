class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # No two vertices have more than one edge and no vertex has an edge to itself
        edges_dict = {}
        for vertex1, vertex2 in edges:
            if vertex1 not in edges_dict:
                edges_dict[vertex1] = [vertex2]
            else:
                edges_dict[vertex1].append(vertex2)
            
            if vertex2 not in edges_dict:
                edges_dict[vertex2] = [vertex1]
            else:
                edges_dict[vertex2].append(vertex1)
        # Work on getting shortest path first
    
        queue = [(0, 1)]
        # We only care about the top two fastest times
        fastest_times = []
        for i in range(n):
            # Fastest is index 0
            fastest_times.append([float('inf'), float('inf')])
        while queue:
            curr_time, curr_node = heapq.heappop(queue)
            updated = False
            if curr_time < fastest_times[curr_node - 1][0]:
                fastest_times[curr_node - 1][0], fastest_times[curr_node - 1][1] = curr_time, fastest_times[curr_node - 1][0]
                updated = True
            elif fastest_times[curr_node - 1][0] < curr_time < fastest_times[curr_node - 1][1]:
                fastest_times[curr_node - 1][1] = curr_time
                updated = True

            if curr_node == n and fastest_times[curr_node - 1][1] != float('inf'):
                return fastest_times[curr_node - 1][1]
            
            if curr_node in edges_dict and updated:
                for new_node in edges_dict[curr_node]:
                    # Light is green
                    if (curr_time // change) % 2 == 0:
                        heapq.heappush(queue, (curr_time + time, new_node))
                    else:
                        heapq.heappush(queue, ((((curr_time // change) + 1) * change) + time, new_node))
        # Should never run
        return -1
            