class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        import sys

        m, n = len(mat), len(mat[0])
        dp = [[sys.maxsize - 1 for _ in range(n)] for _ in range(m)]

        for i in range(0, m):
            for j in range(0, n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        continue
                    elif i == 0:
                        dp[i][j] = min(1 + dp[i][j-1], dp[i][j])
                    elif j == 0:
                        dp[i][j] = min(1 + dp[i-1][j], dp[i][j])
                    else:
                        dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i][j])

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m - 1 and j == n-1:
                    continue
                elif i == m - 1:
                    dp[i][j] = min(dp[i][j + 1] + 1, dp[i][j])
                elif j == n - 1:
                    dp[i][j] = min(dp[i+1][j] + 1, dp[i][j])
                else:
                    dp[i][j] = min(dp[i][j + 1] + 1, dp[i+1][j] + 1, dp[i][j])

        return dp
