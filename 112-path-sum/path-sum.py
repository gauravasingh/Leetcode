# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        queue = deque([(root, root.val)])
        
        while queue:
            node, curr_sum = queue.popleft()
            
            # Check leaf
            if not node.left and not node.right and curr_sum == targetSum:
                return True
            
            if node.left:
                queue.append((node.left, curr_sum + node.left.val))
            if node.right:
                queue.append((node.right, curr_sum + node.right.val))
        
        return False
