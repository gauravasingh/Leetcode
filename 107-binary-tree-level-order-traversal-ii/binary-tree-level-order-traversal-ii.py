# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]  # simple list used as a queue

        while queue:
            level = []
            next_queue = []  # next level nodes
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            res.append(level)
            queue = next_queue  # move to the next level

        return res[::-1]
