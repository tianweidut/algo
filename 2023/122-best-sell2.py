
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        dp = [[0, 0] for _ in range(0, n)]
        for i in range(0, n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]) 
        print(dp)
        return dp[n-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # dp含义：第i天卖出时最大获利
        dp = [0] * n
        max_profit = 0
        for i in range(1, n):
            if prices[i] >= prices[i-1]:
                dp[i] = dp[i-1] + prices[i] - prices[i-1]
            else:
                dp[i] = 0
                max_profit += dp[i - 1]

        max_profit += dp[n-1]
        return max_profit
