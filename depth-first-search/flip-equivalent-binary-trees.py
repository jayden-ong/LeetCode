# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def check_equivalent(root1, root2):
            # Check if the nodes are NULL
            if root1 is None and root2 is not None:
                return False
            elif root1 is not None and root2 is None:
                return False
            elif root1 is None and root2 is None:
                return True
            
            # The nodes have values
            if root1.val != root2.val:
                return False
            
            # They must have the same value
            # The root1 left has to be equivalent to the root2 left or right

            return (check_equivalent(root1.left, root2.right) and check_equivalent(root1.right, root2.left)) or (check_equivalent(root1.left, root2.left) and check_equivalent(root1.right, root2.right))
        return check_equivalent(root1, root2)

            