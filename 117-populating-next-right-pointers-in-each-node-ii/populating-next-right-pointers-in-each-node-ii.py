# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        leftmost = root
        while leftmost:
            # Dummy node to track the head of the next level
            dummy = prev = Node(0)
            curr = leftmost

            # Traverse the current level
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next  # Move to the next node in the same level

            # Move to the next level
            leftmost = dummy.next

        return root
