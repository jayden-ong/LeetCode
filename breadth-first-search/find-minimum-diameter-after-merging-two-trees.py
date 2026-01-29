class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        edges1_dict = defaultdict(list)
        edges2_dict = defaultdict(list)
        for start, end in edges1:
            edges1_dict[start].append(end)
            edges1_dict[end].append(start)
        
        for start, end in edges2:
            edges2_dict[start].append(end)
            edges2_dict[end].append(start)
        
        def determine_diameter(node, edges_dict, curr_best, nodes_explored):
            nodes_explored.add(node)
            children = []
            for end in edges_dict[node]:
                if end not in nodes_explored:
                    children.append(end)
            # If no children, the longest path is 0
            # If one child, the longest path is 1 + the length of that tree's longest path
            # If multiple children, get the two longest paths, add them up and add 2
            if len(children) == 0:
                return 0
            elif len(children) == 1:
                longest_path = determine_diameter(children[0], edges_dict, curr_best, nodes_explored)
                curr_best[0] = max(curr_best[0], longest_path + 1)
                return longest_path + 1
            else:
                longest = None
                second_longest = None
                for child in children:
                    curr_length = determine_diameter(child, edges_dict, curr_best, nodes_explored)
                    if longest is None or curr_length > longest:
                        longest, second_longest = curr_length, longest
                    elif second_longest is None or curr_length > second_longest:
                        second_longest = curr_length
                    
                curr_best[0] = max(curr_best[0], 2 + longest + second_longest)
                # Only return length of longest path
                return longest + 1
        
        diameter1 = [0]
        diameter2 = [0]
        determine_diameter(0, edges1_dict, diameter1, set())
        determine_diameter(0, edges2_dict, diameter2, set())
        # Last option
        first = diameter1[0] // 2 
        if diameter1[0] % 2 == 1:
            first += 1
        
        second = diameter2[0] // 2
        if diameter2[0] % 2 == 1:
            second += 1
            
        answers = [diameter1[0], diameter2[0], first + second + 1]
        return max(answers)