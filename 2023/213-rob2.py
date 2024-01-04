class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def _rob(nums) -> int:
            cur, pre = 0, 0
            for n in nums:
                cur, pre = max(pre + n, cur), cur
            return cur
        return max(_rob(nums[:-1]), _rob(nums[1:]))

    def rob(self, nums) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [0] * n
        dp2 = [0] * n

        for i in range(0, n):
            # rob or not rob
            if i == 0:
                dp[i] = nums[i]
                dp2[i] = 0
            elif i == 1:
                dp[i] = dp[i - 1]
                dp2[i] = nums[i]
            elif i == n - 1:
                dp[i] = dp[i - 1]
                dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
                dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])

        return max(dp[n - 1], dp2[n - 1])

