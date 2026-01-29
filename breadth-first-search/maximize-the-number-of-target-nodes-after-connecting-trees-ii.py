class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        edges_dict1 = defaultdict(set)
        num_nodes = 0
        for start, end in edges1:
            edges_dict1[end].add(start)
            edges_dict1[start].add(end)
            num_nodes = max(num_nodes, max(start, end))
        num_nodes_first = num_nodes + 1
        reds = set()
        blues = set()
        curr_queue = deque()
        curr_queue.append((0, 0))
        visited = set()
        while curr_queue and len(visited) < num_nodes + 1:
            curr_node, curr_distance = curr_queue.popleft()
            if curr_node in visited:
                continue
            else:
                visited.add(curr_node)
                if curr_distance % 2 == 0:
                    reds.add(curr_node)
                else:
                    blues.add(curr_node)
                    
                for new_node in edges_dict1[curr_node]:
                    if new_node not in visited:
                        curr_queue.append((new_node, curr_distance + 1))
        
        edges_dict2 = defaultdict(set)
        num_nodes = 0
        reds2 = set()
        blues2 = set()
        for start, end in edges2:
            edges_dict2[end].add(start)
            edges_dict2[start].add(end)
            num_nodes = max(num_nodes, max(start, end))

        curr_queue = deque()
        curr_queue.append((start, 0))
        visited = set()
        while curr_queue and len(visited) < num_nodes + 1:
            curr_node, curr_distance = curr_queue.popleft()
            if curr_node in visited:
                continue
            else:
                visited.add(curr_node)
                if curr_distance % 2 == 0:
                    reds2.add(curr_node)
                else:
                    blues2.add(curr_node)
                    
                for new_node in edges_dict2[curr_node]:
                    if new_node not in visited:
                        curr_queue.append((new_node, curr_distance + 1))
        
        answers = []
        for i in range(num_nodes_first):
            if i in reds:
                answer = len(reds)
            else:
                answer = len(blues)
            answers.append(answer + max(len(reds2), len(blues2)))
            
        return answers
        
        