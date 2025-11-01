# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._push_left_branch(root)

    def _push_left_branch(self, node):
        """Push all the left children of a node onto the stack."""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        :rtype: int
        Moves the pointer to the next smallest element and returns it.
        """
        # Pop the smallest node
        node = self.stack.pop()

        # If it has a right child, push all left descendants of that right child
        if node.right:
            self._push_left_branch(node.right)

        return node.val

    def hasNext(self):
        """
        :rtype: bool
        Returns true if there exists a next number in the traversal.
        """
        return len(self.stack) > 0
