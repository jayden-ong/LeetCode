# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def fix(root):
            if root.left is not None:
                root.left.val = 2 * root.val + 1
                fix(root.left)
            
            if root.right is not None:
                root.right.val = 2 * root.val + 2
                fix(root.right)
            return root
        root.val = 0
        self.root = fix(root)

    def find(self, target: int) -> bool:
        path = []
        curr = target
        while curr > 0:
            if curr % 2 == 0:
                path.append('right')
                curr -= 2
            else:
                path.append('left')
                curr -= 1
            curr //= 2
        
        path = path[::-1]
        curr_node = self.root
        if curr_node is None:
            return False
        
        for direction in path:
            if direction == 'left':
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
            
            if curr_node is None:
                return False
        return True


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)