# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        in_order = []
        nodes_in_order = {}

        def in_order_trav(root):
            if root.left is not None:
                in_order_trav(root.left)
            
            in_order.append(root.val)
            nodes_in_order[root.val] = root

            if root.right is not None:
                in_order_trav(root.right)
            
            return
        
        in_order_trav(root)
        lower_bound = float('-inf')
        upper_bound = float('inf')

        # Should be increasing
        for i in range(1, len(in_order)):
            if in_order[i - 1] >= in_order[i]:
                starting_point = i - 1
                if starting_point > 0:
                    lower_bound = in_order[starting_point - 1]
                if starting_point < len(in_order) - 1:
                    upper_bound = in_order[starting_point + 1]
                break
        
        ending_point = -1
        for i in range(starting_point + 1, len(in_order) - 1):
            if i == starting_point + 1:
                if in_order[i] > lower_bound and in_order[i] < in_order[starting_point] and in_order[starting_point] < in_order[i + 1]:
                    ending_point = i
                    break
                
            if lower_bound < in_order[i] and in_order[i] < upper_bound and in_order[starting_point] > in_order[i - 1] and in_order[starting_point] < in_order[i + 1]:
                ending_point = i
                break
        
        print(in_order)
        search_num1 = in_order[starting_point]
        node1 = nodes_in_order[search_num1]
        search_num2 = in_order[ending_point]
        node2 = nodes_in_order[search_num2]
        temp = node1.val
        node1.val = node2.val
        node2.val = temp
        print(search_num1)
        print(search_num2)