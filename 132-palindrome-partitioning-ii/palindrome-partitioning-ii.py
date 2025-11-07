class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # 1: Precompute palindrome table
        isPal = [[False] * n for _ in range(n)]
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or isPal[start + 1][end - 1]):
                    isPal[start][end] = True
        
        # 2: DP for minimum cuts
        dp = [0] * n
        for i in range(n):
            if isPal[0][i]:
                dp[i] = 0
            else:
                dp[i] = min(dp[j - 1] + 1 for j in range(1, i + 1) if isPal[j][i])
        
        return dp[-1]
