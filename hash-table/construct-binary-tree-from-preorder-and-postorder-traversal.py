# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        preorder_index = [0]
        postorder_index = [0]
        def construct_tree(curr_node):
            if preorder_index[0] >= len(preorder) or postorder_index[0] >= len(postorder):
                return
            curr_node.val = preorder[preorder_index[0]]
            preorder_index[0] += 1
            # Left - If the postorder val matches the curr_node.val, no more children and return
            if curr_node.val == postorder[postorder_index[0]]:
                # Move to the next node
                postorder_index[0] += 1
                return
            
            if preorder_index[0] >= len(preorder) or postorder_index[0] >= len(postorder):
                return
            curr_node.left = TreeNode()
            construct_tree(curr_node.left)

            # This node cannot have any morder children
            if preorder_index[0] >= len(preorder) or postorder_index[0] >= len(postorder) or postorder[postorder_index[0]] == curr_node.val:
                postorder_index[0] += 1
                return
            curr_node.right = TreeNode()
            construct_tree(curr_node.right)
            # Done with this node, so it should not be considered in postorder
            postorder_index[0] += 1
        
        answer = TreeNode()
        construct_tree(answer)
        print(answer)
        return answer

        