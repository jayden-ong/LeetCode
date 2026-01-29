from collections import deque
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        edges_dict = defaultdict(list)
        for v1, v2, weight in edges:
            edges_dict[v1].append((v2, weight))
            edges_dict[v2].append((v1, weight))
        
        visited_dict = {}
        components = []
        for i in range(n):
            if i not in visited_dict:
                visited_dict[i] = len(components)
                smallest_weight = None
                curr_set = set()
                curr_set.add(i)
                nodes_to_explore = deque()
                nodes_to_explore.append(i)
                while nodes_to_explore:
                    curr_node = nodes_to_explore.popleft()
                    new_nodes = set()
                    for v2, weight in edges_dict[curr_node]:
                        if smallest_weight is None:
                            smallest_weight = weight
                        else:
                            smallest_weight &= weight
                        if v2 not in curr_set:
                            new_nodes.add(v2)
                            nodes_to_explore.append(v2)

                    for node in new_nodes:
                        visited_dict[node] = len(components)
                        curr_set.add(node)

                components.append([smallest_weight, curr_set])
        
        answer = []
        for start, end in query:
            if visited_dict[start] == visited_dict[end]:
                answer.append(components[visited_dict[start]][0])
            else:
                answer.append(-1)
        return answer