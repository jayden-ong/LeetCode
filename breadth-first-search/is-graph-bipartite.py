from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # If there is an edge between two nodes, those two nodes must be in different sets
        set_a = set()
        set_b = set()
        nodes_explored = set()
        for i in range(len(graph)):
            if i not in nodes_explored:
                queue = deque()
                queue.append(i)
                while queue:
                    curr_node = queue.popleft()
                    if curr_node not in set_a and curr_node not in set_b:
                        set_a.add(curr_node)
                    
                    for j in range(len(graph[curr_node])):
                        if curr_node in set_a:
                            if graph[curr_node][j] in set_a:
                                return False
                            set_b.add(graph[curr_node][j])
                        else:
                            if graph[curr_node][j] in set_b:
                                return False
                            set_a.add(graph[curr_node][j])
                        
                        if graph[curr_node][j] not in nodes_explored:
                            queue.append(graph[curr_node][j])
                    nodes_explored.add(curr_node)
        return True