# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Want inorder traversal
        answer = []
        curr_k = [1]
        def recursive(root):
            if root.left is None and root.right is None:
                if curr_k[0] == k:
                    answer.append(root.val)
                curr_k[0] += 1
                return

            if root.left is None:
                if curr_k[0] == k:
                    answer.append(root.val)
                    curr_k[0] += 1
                    return
            else: 
                recursive(root.left)
            
            #print('---')
            #print(root.val)
            #print(curr_k)
            #print(k)
            #print('---')
            if curr_k[0] == k:
                answer.append(root.val)
                curr_k[0] += 1
                return
            elif curr_k[0] > k:
                curr_k[0] += 1
                return
            
            curr_k[0] += 1
            if root.right is not None:
                recursive(root.right)
            return
        
        recursive(root)
        #print(answer)
        return answer[0]