class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        total_XOR = 0
        for num in nums:
            total_XOR ^= num
        
        edges_dict = defaultdict(set)
        for start, end in edges:
            edges_dict[start].add(end)
            edges_dict[end].add(start)
        
        subtree_XOR = [0] * len(nums)
        node_time = [-1] * len(nums)
        curr_time = [0]
        def find_subtree_XOR(root, visited):
            visited.add(root)
            nodes_to_check = []
            for exit_node in edges_dict[root]:
                if exit_node not in visited:
                    nodes_to_check.append(exit_node)
            
            enter_time = curr_time[0]
            curr_time[0] += 1
            curr_XOR = nums[root]
            if nodes_to_check:
                for node in nodes_to_check:
                    curr_XOR ^= find_subtree_XOR(node, visited)
            subtree_XOR[root] = curr_XOR
            exit_time = curr_time[0]
            node_time[root] = [enter_time, exit_time]
            curr_time[0] += 1
            return subtree_XOR[root]

        answer = float('inf')
        find_subtree_XOR(0, set())
        for i in range(len(edges) - 1):
            start1, end1 = edges[i]
            # Want start1 to be parent and end1 to be child
            # Whichever you enter first has to be the parent
            if node_time[start1][0] > node_time[end1][0]:
                start1, end1 = end1, start1
            
            for j in range(i + 1, len(edges)):
                start2, end2 = edges[j]
                if node_time[start2][0] > node_time[end2][0]:
                    start2, end2 = end2, start2
                
                # Want to check if end2 is in the first subtree
                if node_time[end1][0] < node_time[end2][0] < node_time[end2][1] < node_time[end1][1]:
                    first_XOR = subtree_XOR[end2]
                    second_XOR = subtree_XOR[end1] ^ subtree_XOR[end2]
                    third_XOR = total_XOR ^ subtree_XOR[end1]
                elif node_time[end2][0] < node_time[end1][0] < node_time[end1][1] < node_time[end2][1]:
                    first_XOR = subtree_XOR[end1]
                    second_XOR = subtree_XOR[end1] ^ subtree_XOR[end2]
                    third_XOR = total_XOR ^ subtree_XOR[end2]
                else:
                    # Removing the second tree from the XOR that represents everything outside those trees
                    first_XOR = subtree_XOR[end1]
                    second_XOR = subtree_XOR[end2]
                    third_XOR = total_XOR ^ subtree_XOR[end1] ^ subtree_XOR[end2]
                answer = min(answer, max([first_XOR, second_XOR, third_XOR]) - min([first_XOR, second_XOR, third_XOR]))
        return answer