# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Length of the linked list
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        size = get_length(head)
        self.current = head  # pointer that moves as we build the tree

        # Build the BST recursively
        def build_tree(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            # Recursively build left subtree
            left_child = build_tree(left, mid - 1)

            # Create the root with the current list node
            root = TreeNode(self.current.val)
            self.current = self.current.next

            # Recursively build right subtree
            root.left = left_child
            root.right = build_tree(mid + 1, right)

            return root

        return build_tree(0, size - 1)
