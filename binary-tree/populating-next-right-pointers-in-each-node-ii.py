"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        nodes = []
        # Want to get the preorder traversal
        def helper(curr_node, curr_depth):
            if curr_node is None:
                return
            
            if len(nodes) < curr_depth + 1:
                nodes.append([curr_node])
            else:
                nodes[curr_depth].append(curr_node)
            
            if curr_node.left is not None:
                helper(curr_node.left, curr_depth + 1)
            
            if curr_node.right is not None:
                helper(curr_node.right, curr_depth + 1)
        
        helper(root, 0)
        for row in nodes:
            for i in range(len(row) - 1):
                row[i].next = row[i + 1]
        return root