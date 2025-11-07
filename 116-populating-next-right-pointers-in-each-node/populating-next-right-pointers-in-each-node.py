# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        def connectNodes(node1: 'Node', node2: 'Node'):
            if not node1 or not node2:
                return
            
            # Connect node1 -> node2
            node1.next = node2
            
            # Connect children within the same subtree
            connectNodes(node1.left, node1.right)
            connectNodes(node2.left, node2.right)
            
            # Connect across subtrees (right child of left subtree -> left child of right subtree)
            connectNodes(node1.right, node2.left)
        
        connectNodes(root.left, root.right)
        return root
