class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        edges_dict = defaultdict(set)
        i = 0
        for node1, node2 in edges:
            edges_dict[node1].add((node2, succProb[i]))
            edges_dict[node2].add((node1, succProb[i]))
            i += 1
        # hmmm
        probable_paths = [0] * n
        probable_paths[start_node] = 1
        pq = []
        heapq.heappush(pq, (-1, start_node))
        nodes_explored = set()
        while pq and len(nodes_explored) != n:
            curr_prob, curr_node = heapq.heappop(pq)
            curr_prob *= -1
            if curr_node not in nodes_explored:
                probable_paths[curr_node] = curr_prob
                for next_node, next_cost in edges_dict[curr_node]:
                    if next_node not in nodes_explored:
                        heapq.heappush(pq, (-next_cost * curr_prob, next_node))
            nodes_explored.add(curr_node)
        return probable_paths[end_node]