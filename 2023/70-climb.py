class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = {}

        def climb(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2

            if n not in self.dp:
                self.dp[n] = climb(n-1) + climb(n-2)
        
            return self.dp[n]
        return climb(n)
