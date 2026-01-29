# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(root):
            if root is None or (root.left is None and root.right is None):
                return 0
            
            return max(get_height(root.left), get_height(root.right)) + 1
        
        height = get_height(root)
        answer = []
        columns = [""] * (pow(2, height + 1) - 1)
        for i in range(height + 1):
            answer.append(columns.copy())
        # Number of rows should be height + 1
        # Number of cols should be pow(2, height + 1) - 1
        
        def format_tree(root, parent_row, parent_col, is_left):
            if root is None:
                return
            
            # Must be the first node in the tree
            if parent_row is None and parent_col is None and is_left is None:
                curr_row = 0
                curr_col = (pow(2, height + 1) - 2) // 2
            else:
                if is_left:
                    curr_row = parent_row + 1
                    curr_col = parent_col - pow(2, height - parent_row - 1)
                else:
                    curr_row = parent_row + 1
                    curr_col = parent_col + pow(2, height - parent_row - 1)
            answer[curr_row][curr_col] = str(root.val)
            
            if root.left is not None:
                format_tree(root.left, curr_row, curr_col, True)
            
            if root.right is not None:
                format_tree(root.right, curr_row, curr_col, False)
        
        format_tree(root, None, None, None)
        return answer
