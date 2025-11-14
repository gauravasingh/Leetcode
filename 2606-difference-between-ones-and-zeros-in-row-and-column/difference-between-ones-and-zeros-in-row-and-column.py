class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        # Count ones per row & per column
        onesRow = [sum(row) for row in grid]
        onesCol = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        # Build result
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            rowVal = 2 * onesRow[i] - n
            for j in range(n):
                colVal = 2 * onesCol[j] - m
                diff[i][j] = rowVal + colVal
        
        return diff
