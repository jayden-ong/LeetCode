class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        edges_dict = defaultdict(dict)
        for src, dst, weight in edges:
            edges_dict[src][dst] = weight
            edges_dict[dst][src] = weight
        
        def djikstra(edges_dict):
            visited = set()
            pq = [(0, source)]
            while pq:
                curr_weight, curr_node = heapq.heappop(pq)
                if curr_node == destination:
                    return curr_weight
                
                if curr_node not in visited:
                    for dst in edges_dict[curr_node]:
                        if dst not in visited and edges_dict[curr_node][dst] != -1 and edges_dict[curr_node][dst] + curr_weight <= target:
                            heapq.heappush(pq, (edges_dict[curr_node][dst] + curr_weight, dst))
                    
                visited.add(curr_node)
            return float('inf')
        
        shortest_dist = djikstra(edges_dict)
        if shortest_dist < target:
            return []
        
        answer = []
        answer_found = shortest_dist == target
        for src, dst, weight in edges:
            if weight == -1:
                if answer_found:
                    edges_dict[src][dst] = target
                    edges_dict[dst][src] = target
                else:
                    edges_dict[src][dst] = 1
                    edges_dict[dst][src] = 1
                
                    shortest_dist = djikstra(edges_dict)
                    if shortest_dist <= target:
                        answer_found = True
                        edges_dict[src][dst] += target - shortest_dist
                        edges_dict[dst][src] += target - shortest_dist
            answer.append((src, dst, edges_dict[src][dst]))
        if answer_found:
            return answer
        return []
        
            