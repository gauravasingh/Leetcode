class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # If start or end cell is blocked, no path exists
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dp = [0] * n
        dp[0] = 1  # Start position

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # Blocked cell → no paths
                elif j > 0:
                    dp[j] += dp[j - 1]  # Sum of top and left paths

        return dp[-1]
