from collections import deque
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Tree means there is only one route from one node to every other node
        # Because it has to be a valid tree, if n == 1, then there are no edges
        if n == 1:
            return [0]

        edges_dict = {}
        # Want to get every node each node is connected to
        for edge in edges:
            if edge[0] not in edges_dict:
                edges_dict[edge[0]] = {edge[1]}
            else:
                edges_dict[edge[0]].add(edge[1])
            
            if edge[1] not in edges_dict:
                edges_dict[edge[1]] = {edge[0]}
            else:
                edges_dict[edge[1]].add(edge[0])
        
        # dp array
        sum_of_paths = [0] * n
        # number of nodes in subtree
        nodes_in_subtree = [1] * n
        def dfs(curr_node, parent):
            for node in edges_dict[curr_node]:
                if node != parent:
                    dfs(node, curr_node)
                    nodes_in_subtree[curr_node] += nodes_in_subtree[node]
                    sum_of_paths[curr_node] += sum_of_paths[node] + nodes_in_subtree[node]

        def dfs2(curr_node, parent):
            # For resetting later
            old_parent_size = nodes_in_subtree[parent]
            old_parent_sum = sum_of_paths[parent]
            old_node_size = nodes_in_subtree[curr_node]
            old_node_sum = sum_of_paths[curr_node]
            # Rerooting
            nodes_in_subtree[parent] -= nodes_in_subtree[curr_node]
            sum_of_paths[parent] -= sum_of_paths[curr_node] + nodes_in_subtree[curr_node]
            nodes_in_subtree[curr_node] += nodes_in_subtree[parent]
            sum_of_paths[curr_node] += sum_of_paths[parent] + nodes_in_subtree[parent]
            curr_answer[curr_node] = sum_of_paths[curr_node]

            #print(curr_node)
            #print(nodes_in_subtree)
            #print(sum_of_paths)
            for node in edges_dict[curr_node]:
                if node != parent:
                    dfs2(node, curr_node)
            # Resetting
            nodes_in_subtree[parent] = old_parent_size
            sum_of_paths[parent] = old_parent_sum
            nodes_in_subtree[curr_node] += old_node_size
            sum_of_paths[curr_node] += old_node_sum
        # Initialize array
        dfs(0, None)
        curr_answer = [0] * n 
        curr_answer[0] = sum_of_paths[0]
        # Want a stack that is (node, parent)
        for node in edges_dict[0]:
            dfs2(node, 0)
        return curr_answer
        