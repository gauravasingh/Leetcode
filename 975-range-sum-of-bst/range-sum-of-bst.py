# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return
        ans = 0
        if low <= root.val <= high:
            ans += root.val
        if root.val >= low and root.left:
            ans+=self.rangeSumBST(root.left, low, high)
        if root.val <= high and root.right:
            ans+=self.rangeSumBST(root.right, low, high)
        return ans