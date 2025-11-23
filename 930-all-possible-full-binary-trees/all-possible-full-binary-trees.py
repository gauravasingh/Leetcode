# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def helper(num):
            if num in memo:
                return memo[num]

            # Full binary trees must have an odd number of nodes
            if num % 2 == 0:
                return []
            if num == 1:
                return [TreeNode(0)]

            res = []
            # choose odd sizes for left subtree
            for left_nodes in range(1, num, 2):
                right_nodes = num - 1 - left_nodes
                left_trees = helper(left_nodes)
                right_trees = helper(right_nodes)

                for lt in left_trees:
                    for rt in right_trees:
                        root = TreeNode(0)
                        root.left = lt
                        root.right = rt
                        res.append(root)

            memo[num] = res
            return res

        return helper(n)
