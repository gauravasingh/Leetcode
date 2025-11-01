# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Ignore negative paths (take 0 instead)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Price of new path including both children
            current_path_sum = node.val + left_gain + right_gain

            # Update global maximum if needed
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the maximum gain to parent (only one branch)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
