# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0  # pointer over preorder list
        
        def build(lower, upper):
            # If we've used all nodes, stop
            if self.i == len(preorder):
                return None
            
            val = preorder[self.i]
            # If the value doesn't fit the valid BST range, stop
            if not (lower < val < upper):
                return None
            
            # Use this value and build subtree
            self.i += 1
            root = TreeNode(val)
            root.left = build(lower, val)
            root.right = build(val, upper)
            return root
        
        return build(float('-inf'), float('inf'))
