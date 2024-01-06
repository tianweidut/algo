class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    prev = 0
                elif i == 0:
                    prev = dp[0][j-1]
                elif j == 0:
                    prev = dp[i-1][0]
                else:
                    prev = min(dp[i-1][j], dp[i][j-1])
                    
                dp[i][j] = grid[i][j] + prev

        return dp[m-1][n-1]
