# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        n = len(grid)

        def build(r0, c0, length):
            # Check if all cells in this region are the same
            first = grid[r0][c0]
            all_same = True
            for i in range(r0, r0 + length):
                for j in range(c0, c0 + length):
                    if grid[i][j] != first:
                        all_same = False
                        break
                if not all_same:
                    break

            # If uniform, create a leaf node
            if all_same:
                return Node(first == 1, True)

            # Otherwise, divide into 4 quadrants
            half = length // 2
            topLeft = build(r0, c0, half)
            topRight = build(r0, c0 + half, half)
            bottomLeft = build(r0 + half, c0, half)
            bottomRight = build(r0 + half, c0 + half, half)

            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return build(0, 0, n)
