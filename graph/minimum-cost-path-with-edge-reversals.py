class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        edges_dict = defaultdict(set)
        edges_dict_r = defaultdict(set)
        for start, end, cost in edges:
            edges_dict[start].add((end, cost))
            edges_dict_r[end].add((start, 2 * cost))
        
        queue = []
        heapq.heappush(queue, (0, 0, False))
        visited = set()
        visited.add(0)
        while queue:
            # print(queue)
            cost, curr_node, switched = heapq.heappop(queue)
            if curr_node == n - 1:
                return cost
            
            visited.add(curr_node)
            
            for next_node, add_cost in edges_dict[curr_node]:
                if next_node not in visited:
                    heapq.heappush(queue, (cost + add_cost, next_node, switched))
            
            for next_node, add_cost in edges_dict_r[curr_node]:
                if next_node not in visited:
                    heapq.heappush(queue, (cost + add_cost, next_node, True))
            
        return -1