class UnionFind:
        def __init__(self, size):
            self.parent = []
            for i in range(size):
                self.parent.append(i)
        
        def find_rep(self, curr_node):
            if self.parent[curr_node] == curr_node:
                return curr_node
            return self.find_rep(self.parent[curr_node])
        
        def union(self, node1, node2):
            rep1 = self.find_rep(node1)
            rep2 = self.find_rep(node2)
            self.parent[rep2] = rep1

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # Must contain n - 1 edges
        # All edges with must == 1, must be included in the spanning tree
        # If an edge is required, put both nodes in the same group
        edges_by_strength = []
        required_edges = []
        max_strength = float('-inf')
        for node1, node2, strength, required in edges:
            if required:
                required_edges.append((strength, node1, node2))
                max_strength = max(max_strength, strength)
            else:
                edges_by_strength.append((strength, node1, node2)) 
                max_strength = max(max_strength, 2 * strength)
        edges_by_strength.sort(reverse=True)

        # The required edges dictate the absolute maximum answer
        # It could still go lower
        min_strength = answer = 0
        def determine_possible(required_strength):
            num_edges = 0
            num_boosts = k
            dsu = UnionFind(n)
            curr_strength = float('inf')
            # Add required edges first
            for strength, node1, node2 in required_edges:
                dsu.union(node1, node2)
                curr_strength = min(curr_strength, strength)
                num_edges += 1
            
            if curr_strength < required_strength:
                return False
            
            if num_edges == n - 1:
                return True
            
            # We can only add edges that causes a change to the reps
            for strength, node1, node2 in edges_by_strength:
                if dsu.find_rep(node1) != dsu.find_rep(node2):
                    dsu.union(node1, node2)
                    # Return false if smaller and out of boosts or boost is useless
                    if strength < required_strength:
                        if num_boosts == 0 or 2 * strength < required_strength:
                            return False
                        num_boosts -= 1
                    
                    num_edges += 1
                    if num_edges == n - 1:
                        return True
            return False

        answer = -1
        while min_strength <= max_strength:
            mid = (min_strength + max_strength) // 2
            if determine_possible(mid):
                answer = mid
                min_strength = mid + 1
            else:
                max_strength = mid - 1
        return answer