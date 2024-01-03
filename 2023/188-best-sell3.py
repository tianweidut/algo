class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[[0, 0] for _ in range(k+1)] for _ in range(n)]

        for i in range(0, n):
            for j in range(1, k+1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        return dp[n-1][k][0]
