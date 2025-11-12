# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return (0, 0, 0)  # (sum, count, matches)
            
            l_sum, l_count, l_matches = dfs(node.left)
            r_sum, r_count, r_matches = dfs(node.right)
            
            total_sum = l_sum + r_sum + node.val
            total_count = l_count + r_count + 1
            
            # current node matches if its value equals floor of average
            match = 1 if node.val == total_sum // total_count else 0
            
            return (total_sum, total_count, l_matches + r_matches + match)
        
        return dfs(root)[2]
