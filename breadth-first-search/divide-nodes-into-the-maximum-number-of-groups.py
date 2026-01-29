from collections import deque
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # All nodes with no edges can be put in their own group
        edges_dict = defaultdict(set)
        for node1, node2 in edges:
            edges_dict[node1].add(node2)
            edges_dict[node2].add(node1)
        
        def check_bipartite():
            # Will use 1 and -1
            node_colors = defaultdict(int)
            for i in range(1, n + 1):
                if node_colors[i] == 0:
                    nodes_queue = deque()
                    nodes_queue.append(i)
                    node_colors[i] = 1
                    while nodes_queue:
                        curr_node = nodes_queue.popleft()
                        for node in edges_dict[curr_node]:
                            if node_colors[node] == node_colors[curr_node]:
                                return False
                            elif node_colors[node] == node_colors[curr_node] * -1:
                                continue
                            else:
                                node_colors[node] = -1 * node_colors[curr_node]
                                nodes_queue.append(node)
                            
            return True

        def get_height(root):
            nodes_queue = deque()
            nodes_explored = set()
            nodes_explored.add(root)
            nodes_queue.append((root, 0))
            answer = 0
            while nodes_queue:
                curr_node, curr_height = nodes_queue.popleft()
                for neighbour in edges_dict[curr_node]:
                    if neighbour not in nodes_explored:
                        nodes_queue.append((neighbour, curr_height + 1))
                        answer = max(answer, curr_height + 1)
                        nodes_explored.add(neighbour)
            return answer

        if not check_bipartite():
            return -1
        
        heights = []
        for i in range(1, n + 1):
            heights.append(get_height(i))
        
        # Divide nodes into components
        components = []
        nodes_done = set()
        for i in range(1, n + 1):
            if i not in nodes_done:
                nodes_queue = deque()
                nodes_queue.append(i)
                nodes_done.add(i)
                component = [i]
                while nodes_queue:
                    curr_node = nodes_queue.popleft()
                    for node in edges_dict[curr_node]:
                        if node not in nodes_done:
                            component.append(node)
                            nodes_done.add(node)
                            nodes_queue.append(node)
                components.append(component)
        
        answer = 0
        for component in components:
            curr_max = 0
            for node in component:
                # Number of groups is height + 1
                curr_max = max(curr_max, heights[node - 1] + 1)
            answer += curr_max
        return answer