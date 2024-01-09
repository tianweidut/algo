class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for i in range(0, amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != amount +1 else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        import sys

        self.memo = {}

        def dfs(remain):
            if remain == 0:
                return 0

            if remain < 0:
                return -1

            if remain in self.memo:
                return self.memo[remain]

            choice = sys.maxsize 
            for coin in coins:
                res = dfs(remain - coin)
                if res == -1:
                    continue
                choice = min(choice, res + 1)

            self.memo[remain] = -1 if choice == sys.maxsize else choice
            return self.memo[remain]

        return dfs(remain=amount)
