class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def make_graph(conditions):
            parent_to_children = {}
            for i in range(1, k + 1):
                parent_to_children[i] = set()
            
            for above, below in conditions:
                parent_to_children[above].add(below)

            return parent_to_children

        '''
        def check_for_cycle(parent_to_children, source_node, nodes_seen, nodes_checked):
            # nodes_seen will act like our stack call
            nodes_seen.add(source_node)
            for neighbour in parent_to_children[source_node]:
                if neighbour in nodes_seen:
                    return True
                
                if check_for_cycle(parent_to_children, neighbour, nodes_seen, nodes_checked):
                    return True

            nodes_seen.remove(source_node)
            nodes_checked.add(source_node)
            return False
       '''

        # Perform topological ordering
        def dfs(parent_to_children, source_node, nodes_seen, nodes_added, ordering):
            nodes_seen.add(source_node)
            for neighbour in parent_to_children[source_node]:
                # Means cycle exists
                if neighbour in nodes_seen:
                    return True
                
                if neighbour not in nodes_added:
                    if dfs(parent_to_children, neighbour, nodes_seen, nodes_added, ordering):
                        return True

            nodes_seen.remove(source_node)
            nodes_added.add(source_node)
            ordering.append(source_node)
            return False
        # Will stop us from exploring nodes we have already explored
        parent_to_children = make_graph(rowConditions)

        row_nodes_added = set()
        row_ordering = []
        for i in range(1, k + 1):
            if i not in row_nodes_added:
                if dfs(parent_to_children, i, set(), row_nodes_added, row_ordering):
                    return []
        row_ordering = row_ordering[::-1]
        #print(row_ordering)
        
        parent_to_children = make_graph(colConditions)
        col_nodes_added = set()
        col_ordering = []
        for i in range(1, k + 1):
            if i not in col_nodes_added:
                if dfs(parent_to_children, i, set(), col_nodes_added, col_ordering):
                    return []
        col_ordering = col_ordering[::-1]
        #print(col_ordering)

        # Have to form final matrix
        answer = []
        all_rows = [0] * k
        coords_dict = {}
        for i in range(k):
            answer.append(all_rows.copy())
            coords_dict[i + 1] = [0, 0]
        
        for i in range(k):
            coords_dict[row_ordering[i]][0] = i
            coords_dict[col_ordering[i]][1] = i
        
        for num in coords_dict:
            row_num, col_num = coords_dict[num]
            answer[row_num][col_num] = num
        return answer
        
