class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # The search to find safe nodes ends after len(n) steps
        def detect_cycle(curr_node, nodes_seen, nodes_checked):
            if curr_node in nodes_checked:
                return False
            
            if curr_node in nodes_seen:
                return True
            
            nodes_seen.add(curr_node)
            for new_node in graph[curr_node]:
                if detect_cycle(new_node, nodes_seen, nodes_checked):
                    return True
            nodes_seen.remove(curr_node)
            nodes_checked.add(curr_node)
            return False
        
        answer = []
        nodes_checked = set()
        for i in range(len(graph)):
            # If a node has to go to a safe node, that node is safe
            if not detect_cycle(i, set(), nodes_checked):
                answer.append(i)
        return answer

            