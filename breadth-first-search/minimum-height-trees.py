from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        edges_dict = {}
        num_edges = 0
        for edge in edges:
            num_edges += 1
            if edge[0] not in edges_dict:
                edges_dict[edge[0]] = [edge[1]]
            else:
                edges_dict[edge[0]].append(edge[1])
            
            if edge[1] not in edges_dict:
                edges_dict[edge[1]] = [edge[0]]
            else:
                edges_dict[edge[1]].append(edge[0])
        
        if num_edges == 0:
            return [0]
        
        # Find furthest node from node 0
        stack = deque([(0, 0)])
        tallest = -1
        searched = {}
        furthest = 0
        while stack:
            curr_height, curr_node = stack.pop()
            if curr_node not in searched:
                for element in edges_dict[curr_node]:
                    if element not in searched:
                        stack.append((curr_height + 1, element))
            if tallest < curr_height:
                tallest = curr_height
                furthest = curr_node
            searched[curr_node] = True

        # Find furthest node from node furthest
        # Will store the current node path
        stack = deque([(0, [furthest])])
        largest_distance = -1
        searched = {}
        largest_path = []
        while stack:
            curr_height, curr_path = stack.pop()
            curr_node = curr_path[-1]
            if curr_node not in searched:
                for element in edges_dict[curr_node]:
                    temp = curr_path.copy()
                    temp.append(element)
                    if element not in searched:
                        stack.append((curr_height + 1, temp))
            if largest_distance < curr_height:
                largest_distance = curr_height
                largest_path = curr_path
            searched[curr_node] = True

        if largest_distance % 2 == 0:
            return [largest_path[(largest_distance + 1) // 2]]
        return [largest_path[(largest_distance + 1) // 2], largest_path[(largest_distance - 1) // 2]]