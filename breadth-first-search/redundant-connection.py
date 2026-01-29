class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        node_parent = []
        for i in range(len(edges) + 1):
            node_parent.append(i)
        rank = [1] * (len(edges) + 1)

        def find(node):
            # Make searching faster later
            while node != node_parent[node]:
                node_parent[node] = node_parent[node_parent[node]]
                node = node_parent[node]
            return node

        # Nothing to combine
        def combine(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return False
            
            # Want to make the larger rank the parent
            if rank[parent1] > rank[parent2]:
                node_parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                node_parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True
        
        for node1, node2 in edges:
            if not combine(node1, node2):
                return [node1, node2]
            
