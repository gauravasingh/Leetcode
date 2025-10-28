# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        preorder_index = [0]

        def build(left, right):
            if left > right:
                return None

            root_val = preorder[preorder_index[0]]
            preorder_index[0] += 1

            root = TreeNode(root_val)
            inorder_pos = inorder_index[root_val]

            root.left = build(left, inorder_pos - 1)
            root.right = build(inorder_pos + 1, right)

            return root

        return build(0, len(inorder) - 1)
