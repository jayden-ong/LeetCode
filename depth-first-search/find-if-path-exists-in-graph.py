class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        edges_dict = {}
        for edge in edges:
            if edges_dict.get(edge[0], -1) == -1:
                edges_dict[edge[0]] = [edge[1]]
            else:
                edges_dict[edge[0]].append(edge[1])
            
            if edges_dict.get(edge[1], -1) == -1:
                edges_dict[edge[1]] = [edge[0]]
            else:
                edges_dict[edge[1]].append(edge[0])
        
        nodes_explored = {}
        curr_nodes = [source]
        while curr_nodes:
            curr_node = curr_nodes.pop()
            if curr_node == destination:
                return True
            
            if nodes_explored.get(curr_node, -1) == -1:
                curr_nodes.extend(edges_dict[curr_node])
            nodes_explored[curr_node] = True
        return False