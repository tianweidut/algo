class A:
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        k = 2
        dp = [[[0, 0] for _ in range(k+1)] for _ in range(n)]

        for i in range(0, n):
            for j in range(1, k + 1):
                if i - 1 == -1:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                else:
                    # case: reset no + sell and reset no
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                    # case: reset have + new buy
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[n - 1][k][0]

print(A().maxProfit([3,3,5,0,0,3,1,4]))
