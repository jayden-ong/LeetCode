# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert_val(root):
            # Assume root is not none
            if val < root.val:
                if root.left is None:
                    root.left = TreeNode(val, None, None)
                else:
                    insert_val(root.left)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val, None, None)
                else:
                    insert_val(root.right)
            return
        
        if root is None:
            return TreeNode(val, None, None)
        insert_val(root)
        return root