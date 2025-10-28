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
        
        leftmost = root  # Start with the root
        
        while leftmost:
            dummy = Node(0)  # Dummy head for next level
            prev = dummy
            curr = leftmost  # Traverse the current level
            
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next  # Move along current level
            
            leftmost = dummy.next  # Move to next level
        
        return root
