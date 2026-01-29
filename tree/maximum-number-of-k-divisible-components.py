class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Sum of all node values will be divisible by k
        edges_dict = defaultdict(list)
        for start, end in edges:
            edges_dict[start].append(end)
            edges_dict[end].append(start)
        
        nodes_explored = set()
        num_comp = [1]
        # Will return sum of values
        def process_root(root):
            children = []
            nodes_explored.add(root)
            for end in edges_dict[root]:
                if end not in nodes_explored:
                    children.append(end)
            if len(children) == 0:
                if values[root] % k == 0:
                    return 0
                return values[root]
            else:
                curr_value = values[root]
                for child in children:
                    leftover = process_root(child)
                    if leftover == 0:
                        num_comp[0] += 1
                    else:
                        curr_value += leftover
                
                if curr_value % k == 0:
                    return 0
                return curr_value
        
        process_root(0)
        return num_comp[0]
                    