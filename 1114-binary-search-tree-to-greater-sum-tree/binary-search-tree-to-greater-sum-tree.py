# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.running_sum = 0

        def reverse_inorder(node):
            if not node:
                return
            
            # Visit right (greater values)
            reverse_inorder(node.right)
            
            # Process current node
            self.running_sum += node.val
            node.val = self.running_sum
            
            # Visit left (smaller values)
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root
