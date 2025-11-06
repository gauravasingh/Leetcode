class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1  # Base cases

        # dp[i] = sum(dp[left] * dp[right]) for all possible root positions
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                dp[nodes] += dp[left] * dp[right]
        
        return dp[n]
