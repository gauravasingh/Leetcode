# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        old_to_new = {}  # maps original nodes to their cloned copies

        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]
            
            # Clone the node
            copy = Node(curr.val)
            old_to_new[curr] = copy

            # Clone neighbors recursively
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        return dfs(node)
