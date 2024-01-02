class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
