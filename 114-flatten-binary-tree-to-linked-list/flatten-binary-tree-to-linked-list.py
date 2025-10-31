# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root):
        self.prev = None

        def helper(node):
            if not node:
                return
            helper(node.right)
            helper(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node

        helper(root)
