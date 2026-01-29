class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        new_edges = {}
        for src, dest, weight in edges:
            if src not in new_edges:
                new_edges[src] = {}
            new_edges[src][dest] = weight
        
            if dest not in new_edges:
                new_edges[dest] = {}
            new_edges[dest][src] = weight
        
        # Want to use Djikstra's
        best_case = float('inf')
        answer = 0
        for i in range(n):
            shortest_paths = [float('inf')] * n
            shortest_paths[i] = 0
            queue = [(0, i)]
            nodes_visited = set()
            while queue and len(nodes_visited) < n:
                total_weight, curr_node = heapq.heappop(queue)
                if curr_node in new_edges:
                    for new_node in new_edges[curr_node]:
                        if new_node not in nodes_visited:
                            heapq.heappush(queue, (total_weight + new_edges[curr_node][new_node], new_node))
                            shortest_paths[new_node] = min(shortest_paths[new_node], total_weight + new_edges[curr_node][new_node])
                nodes_visited.add(curr_node)
            
            num_cities = 0
            for j in range(n):
                if i != j and shortest_paths[j] <= distanceThreshold:
                    num_cities += 1
            
            if num_cities <= best_case:
                best_case = num_cities
                answer = i
        return answer