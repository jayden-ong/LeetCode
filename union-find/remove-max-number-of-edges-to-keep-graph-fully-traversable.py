class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        node_parent_alice = []
        node_parent_bob = []
        for i in range(n + 1):
            node_parent_alice.append(i)
            node_parent_bob.append(i)
        rank_alice = [1] * (n + 1)
        rank_bob = [1] * (n + 1)
        alice_segs = [n]
        bob_segs = [n]

        def find(node_parent, node):
            # Make searching faster later
            while node != node_parent[node]:
                node_parent[node] = node_parent[node_parent[node]]
                node = node_parent[node]
            return node

        # Nothing to combine
        def combine(node_parent, rank, segs, node1, node2):
            parent1, parent2 = find(node_parent, node1), find(node_parent, node2)
            if parent1 == parent2:
                return False
            
            # Want to make the larger rank the parent
            if rank[parent1] > rank[parent2]:
                node_parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                node_parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            segs[0] -= 1
            return True
        
        answer = 0
        for curr_type, node1, node2 in edges:
            if curr_type == 3:
                res1 = combine(node_parent_alice, rank_alice, alice_segs, node1, node2) 
                res2 = combine(node_parent_bob, rank_bob, bob_segs, node1, node2)
                if res1 or res2:
                    answer += 1
        
        for curr_type, node1, node2 in edges:
            if curr_type == 1:
                if combine(node_parent_alice, rank_alice, alice_segs, node1, node2):
                    answer += 1
            elif curr_type == 2:
                if combine(node_parent_bob, rank_bob, bob_segs, node1, node2):
                    answer += 1
        
        if alice_segs == [1] and bob_segs == [1]:
            return len(edges) - answer
        return -1
        
        
