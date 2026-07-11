class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        edges_dict = defaultdict(set)
        for start, end in edges:
            edges_dict[start].add(end)
            edges_dict[end].add(start)
        
        components = []
        curr_index = 0
        nodes_to_component = {}
        for i in range(n):
            if i not in nodes_to_component:
                curr_component = set()
                curr_component.add(i)
                queue = deque()
                queue.append(i)
                nodes_to_component[i] = curr_index
                while queue:
                    curr_node = queue.popleft()
                    for end_node in edges_dict[curr_node]:
                        if end_node not in curr_component:
                            curr_component.add(end_node)
                            nodes_to_component[end_node] = curr_index
                            queue.append(end_node)
                curr_index += 1
                components.append(curr_component)

        answer = [True] * len(components)
        for curr_node in edges_dict:
            if len(edges_dict[curr_node]) != len(components[nodes_to_component[curr_node]]) - 1:
                answer[nodes_to_component[curr_node]] = False
        return sum(answer)