# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            
            # The current node must be strictly within bounds
            if not (low < node.val < high):
                return False
            
            # Left subtree must be less than node.val
            # Right subtree must be greater than node.val
            return (helper(node.left, low, node.val) and
                    helper(node.right, node.val, high))
        
        return helper(root)
