class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        num_nodes = len(edges)
        def find_distances(starting_node):
            curr_queue = deque()
            curr_queue.append((starting_node, 0))
            visited = set()
            answer = [float('inf')] * num_nodes
            while curr_queue and len(visited) < num_nodes:
                curr_node, curr_distance = curr_queue.popleft()
                if curr_node in visited:
                    continue
                
                visited.add(curr_node)
                answer[curr_node] = curr_distance
                if edges[curr_node] != -1 and edges[curr_node] not in visited:
                    curr_queue.append((edges[curr_node], curr_distance + 1))
            return answer
        
        node1_distances = find_distances(node1)
        node2_distances = find_distances(node2)
        print(node1_distances)
        print(node2_distances)
        
        min_distance = float('inf')
        answer = None
        for i in range(num_nodes):
            if max(node1_distances[i], node2_distances[i]) < min_distance:
                answer = i
                min_distance = max(node1_distances[i], node2_distances[i])
        
        if answer is None:
            return -1
        return answer