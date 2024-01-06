class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 0:
            return []

        dp = [[1 for _ in range(0, i + 1)] for i in range(numRows)]

        for i in range(1, numRows):
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    continue
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        return dp
