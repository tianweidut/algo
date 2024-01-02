class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [0] * n
        l_min = prices[0]
        for i in range(1, n):
            dp[i] = max(0, prices[i] - l_min)
            l_min = min(l_min, prices[i])

        return max(dp)
