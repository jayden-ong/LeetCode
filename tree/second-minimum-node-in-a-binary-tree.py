# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return -1
        
        # The root tells us the smallest value in the entire tree
        curr_smallest = root.val
        # Path from root to leaf has to be non-decreasing
        # Once we find a value larger than the smallest in a subtree, stop searching
        def find_next_smallest(root, smallest):
            if root is None:
                return -1
            
            if root.left is None and root.right is None and root.val == smallest:
                return -1
            
            # The smallest in left subtree must be root.left.val
            if root.left.val != smallest:
                left_smallest = root.left.val
            else:
                left_smallest = find_next_smallest(root.left, smallest)
            
            # The smallest in right subtree must be root.right.val
            if root.right.val != smallest:
                right_smallest = root.right.val
            else:
                right_smallest = find_next_smallest(root.right, smallest)
            
            if left_smallest == -1 and right_smallest == -1:
                return -1
            elif left_smallest == -1:
                return right_smallest
            elif right_smallest == -1:
                return left_smallest
            else:
                return min(right_smallest, left_smallest)
        
        return find_next_smallest(root, curr_smallest)
            