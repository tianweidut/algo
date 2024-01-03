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
                dp[i][1] = max(dp[i-1][1], - prices[i]) 

        return dp[n-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [0] * n
        l_min = prices[0]
        for i in range(1, n):
            dp[i] = max(0, prices[i] - l_min)
            l_min = min(l_min, prices[i])

        return max(dp)
