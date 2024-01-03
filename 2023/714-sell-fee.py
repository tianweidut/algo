class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0, 0] for _ in range(n)]

        for i in range(0, n):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i] - fee
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)

        return dp[n-1][0]
