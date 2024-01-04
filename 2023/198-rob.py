class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [0] * n

        for i in range(0, n):
            # rob or not rob
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(dp[i - 1], nums[i])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[n - 1]
