class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        max_square = 0

        for i in range(0, m):
            for j in range(0, n):
                val = 1 if matrix[i][j] == "1" else 0

                if val != 1:
                    continue

                if i == 0 or j == 0:
                    dp[i][j] = val
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                max_square = max(max_square, dp[i][j] * dp[i][j])

        return max_square
