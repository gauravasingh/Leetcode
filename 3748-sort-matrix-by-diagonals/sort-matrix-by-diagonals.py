class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        n = len(grid)
        diagonals = defaultdict(list)

        # Group elements by diagonal index
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])

        # Sort diagonals appropriately
        for d in diagonals:
            if d >= 0:
                diagonals[d].sort(reverse=True)
            else:
                diagonals[d].sort()

        # Fill back sorted values
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)

        return grid
