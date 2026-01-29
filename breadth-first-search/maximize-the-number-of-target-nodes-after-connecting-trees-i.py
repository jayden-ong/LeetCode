class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        # Need to figure out maximum number of nodes target for each distance 0 to k - 1
        tree1_dp = defaultdict(list)
        edges_dict1 = defaultdict(set)
        num_nodes = 0
        for start, end in edges1:
            edges_dict1[end].add(start)
            edges_dict1[start].add(end)
            num_nodes = max(num_nodes, max(start, end))
        
        max_targets1 = [0] * (num_nodes + 1)
        for start in edges_dict1:
            curr_queue = deque()
            curr_queue.append((start, 0))
            visited = set()
            while curr_queue:
                curr_node, curr_distance = curr_queue.popleft()
                if curr_distance > k:
                    break
                elif curr_node in visited:
                    continue
                else:
                    visited.add(curr_node)
                    for new_node in edges_dict1[curr_node]:
                        if new_node not in visited:
                            curr_queue.append((new_node, curr_distance + 1))
            max_targets1[start] = len(visited)
        
        edges_dict2 = defaultdict(set)
        num_nodes = 0
        # highest_degree = 0
        for start, end in edges2:
            edges_dict2[end].add(start)
            edges_dict2[start].add(end)
            num_nodes = max(num_nodes, max(start, end))

        max_targets2 = [0] * (num_nodes + 1)
        best_node, most_targets = None, 0
        for start in edges_dict2:
            curr_queue = deque()
            curr_queue.append((start, 0))
            visited = set()
            while curr_queue:
                curr_node, curr_distance = curr_queue.popleft()
                if curr_distance > k - 1:
                    break
                elif curr_node in visited:
                    continue
                else:
                    visited.add(curr_node)
                    for new_node in edges_dict2[curr_node]:
                        if new_node not in visited:
                            curr_queue.append((new_node, curr_distance + 1))
            max_targets2[start] = len(visited)
            if max_targets2[start] > most_targets:
                best_node, most_targets = start, max_targets2[start]
        
        answers = []
        for i in range(len(max_targets1)):
            answers.append(max_targets1[i] + most_targets)
            
        return answers