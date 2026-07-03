class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        edges_dict = defaultdict(list)
        for start, end, cost in edges:
            edges_dict[start].append((end, cost))
        queue, visited = deque(), set()
        queue.append((0, float('inf'), 0))
        answer = -1
        while queue:
            node, lowest_cost, total_cost = queue.popleft()
            if node == len(online) - 1:
                answer = max(answer, lowest_cost)
                continue
            
            for dest, cost in edges_dict[node]:
                if cost + total_cost <= k and online[dest]:
                    queue.append((dest, min(cost, lowest_cost), cost + total_cost))

        return answer
