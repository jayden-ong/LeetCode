# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        levels_dict = defaultdict(set)
        levels_max = defaultdict(int)
        levels_second_max = defaultdict(int)
        depth_dict = {}
        def get_height(root, curr_level):
            if root is None:
                return 0
            
            levels_dict[root.val] = curr_level
            # Need to get depth of left and right
            maximum_depth = max(get_height(root.left, curr_level + 1), get_height(root.right, curr_level + 1)) + 1

            if maximum_depth > levels_max[curr_level]:
                levels_second_max[curr_level] = levels_max[curr_level]
                levels_max[curr_level] = maximum_depth
            elif maximum_depth > levels_second_max[curr_level]:
                levels_second_max[curr_level] = maximum_depth
            depth_dict[root.val] = maximum_depth
            return maximum_depth
        get_height(root, 0)
        
        print(levels_dict)
        print(levels_max)
        print(levels_second_max)
        print(depth_dict)
        
        answer = []
        for query in queries:
            curr_level = levels_dict[query]
            curr_depth = depth_dict[query]
            if curr_depth == levels_max[curr_level]:
                answer.append(levels_second_max[curr_level] + curr_level - 1)
            else:
                answer.append(levels_max[curr_level] + curr_level - 1)

        return answer
        