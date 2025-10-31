# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Build a hashmap to quickly find the root in inorder
        idx_map = {val: i for i, val in enumerate(inorder)}
        post_idx = len(postorder) - 1  # Start from the end of postorder

        # Recursive function using closure over post_idx
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal post_idx
            if in_left > in_right:
                return None

            # Get the current root value
            root_val = postorder[post_idx]
            post_idx -= 1

            # Create the root node
            root = TreeNode(root_val)

            # Find index in inorder
            idx = idx_map[root_val]

            # Build subtrees: right first, then left
            root.right = helper(idx + 1, in_right)
            root.left = helper(in_left, idx - 1)

            return root

        return helper(0, len(inorder) - 1)
