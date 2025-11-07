# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, current_sum):
            if not node:
                return

            # Include this node in the path
            path.append(node.val)
            current_sum += node.val

            # CheckingIf it's a leaf & sums up to targetSum & then add to result
            if not node.left and not node.right and current_sum == targetSum:
                res.append(path[:])  # append a copy of the current path

            # Children
            dfs(node.left, path, current_sum)
            dfs(node.right, path, current_sum)

            # Backtrack
            path.pop()

        dfs(root, [], 0)
        return res
