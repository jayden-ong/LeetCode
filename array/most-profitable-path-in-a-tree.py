from collections import deque
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        edges_dict = defaultdict(set)
        for node1, node2 in edges:
            edges_dict[node1].add(node2)
            edges_dict[node2].add(node1)
        
        # Have to first figure out which nodes bob will reach at each turn
        def find_bob_path(curr_node, nodes_explored, curr_path):
            if curr_node == 0:
                return True
            
            for adj in edges_dict[curr_node]:
                if adj not in nodes_explored:
                    nodes_explored.add(adj)
                    curr_path.append(adj)
                    if find_bob_path(adj, nodes_explored, curr_path):
                        return True
                    nodes_explored.remove(adj)
                    curr_path.pop()
            return False
        
        nodes_explored = set()
        nodes_explored.add(bob)
        bob_path = [bob]
        find_bob_path(bob, nodes_explored, bob_path)
        
        bob_node_to_turn = {}
        for i, node in enumerate(bob_path):
            bob_node_to_turn[node] = i

        nodes_queue = deque()
        nodes_queue.append((amount[0], 0, 0))
        nodes_explored = set()
        nodes_explored.add(0)
        answer = None
        while nodes_queue:
            curr_score, curr_node, curr_turn = nodes_queue.popleft()
            for adj in edges_dict[curr_node]:
                if adj not in nodes_explored:
                    new_score = curr_score
                    if curr_turn + 1 < len(bob_path) and bob_path[curr_turn + 1] == adj:
                        new_score += amount[adj] // 2
                    elif adj not in bob_node_to_turn or bob_node_to_turn[adj] > curr_turn + 1:
                        new_score += amount[adj]
                    nodes_queue.append((new_score, adj, curr_turn + 1))
                    nodes_explored.add(adj)
            
            # Is a leaf node
            if curr_node != 0 and len(edges_dict[curr_node]) == 1:
                if answer is None or curr_score > answer:
                    answer = curr_score
            
        return answer
        