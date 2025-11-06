# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None
        cur = root

        while cur:
            if not cur.left:
                # Process current node
                if prev and prev.val > cur.val:
                    if not first:
                        first = prev
                    second = cur
                prev = cur
                cur = cur.right
            else:
                # Find inorder predecessor
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    if prev and prev.val > cur.val:
                        if not first:
                            first = prev
                        second = cur
                    prev = cur
                    cur = cur.right

        # Swap misplaced values
        first.val, second.val = second.val, first.val
        