# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # First char is always a node
        answer = TreeNode()
        num_dashes = 0
        curr_num = ""
        nodes_list = []
        i = 0
        while i <= len(traversal):
            if i == len(traversal) or traversal[i] == "-":
                if curr_num != "":
                    nodes_list.append((num_dashes, int(curr_num)))
                    num_dashes = 1
                    curr_num = ""
                else:
                    num_dashes += 1
            else:
                curr_num += traversal[i]
            i += 1
        print(nodes_list)
        node_index = [0]
        def recover_tree(curr_node):
            # Get the data for the node
            node_depth, curr_node.val = nodes_list[node_index[0]]
            node_index[0] += 1
            # Means there is another node that has to be a child of the root
            for i in range(2):
                if node_index[0] < len(nodes_list):
                    # Need to take a peak at the next node
                    if nodes_list[node_index[0]][0] == node_depth + 1:
                        if i == 0:
                            curr_node.left = TreeNode()
                            recover_tree(curr_node.left)
                        else:
                            curr_node.right = TreeNode()
                            recover_tree(curr_node.right)
                    # This node has no more children -- nothing left to do
                    else:
                        return
            return
                
        recover_tree(answer)
        return answer
        