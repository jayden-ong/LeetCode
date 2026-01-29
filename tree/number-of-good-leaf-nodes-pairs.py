from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # Use post-order label to get rid of duplicate nodes
        curr_label = [0]
        def label(root):
            if root.left is not None:
                label(root.left)
            
            root.val = curr_label[0]
            curr_label[0] += 1

            if root.right is not None:
                label(root.right)
            return

        label(root)
        
        child_to_parent_dict = {}
        def populate_dict(root):
            if root.left is not None:
                child_to_parent_dict[root.left.val] = [False, root]
                populate_dict(root.left)
            
            if root.right is not None:
                child_to_parent_dict[root.right.val] = [False, root]
                populate_dict(root.right)
            
            if root.left is None and root.right is None and root.val in child_to_parent_dict:
                child_to_parent_dict[root.val][0] = True
            
            return
        
        populate_dict(root)
        def dfs(root, starting_val):
            # Will be passing in parent
            queue = deque()
            queue.append((1, root))
            answer = 0
            visited = set()
            visited.add(starting_val)
            while queue:
                curr_distance, curr_node = queue.popleft()
                if curr_distance <= distance and curr_node.left is None and curr_node.right is None:
                    print(starting_val)
                    print(curr_node.val)
                    answer += 1
                else:
                    # Can only continue moving if we have not already moved the max distance
                    # Could go up or could go down
                    if curr_distance < distance:
                        if curr_node.val in child_to_parent_dict and child_to_parent_dict[curr_node.val][1].val not in visited:
                            queue.append((curr_distance + 1, child_to_parent_dict[curr_node.val][1]))
                        
                        # Make sure we don't go back the path we came from
                        if curr_node.left is not None and curr_node.left.val not in visited:
                            queue.append((curr_distance + 1, curr_node.left))
                        
                        if curr_node.right is not None and curr_node.right.val not in visited:
                            queue.append((curr_distance + 1, curr_node.right))
                    visited.add(curr_node.val)
            return answer
        
        answer = 0
        for val in child_to_parent_dict:
            if child_to_parent_dict[val][0]:
                answer += dfs(child_to_parent_dict[val][1], val)
        return answer // 2
        