# [1,5,11,5]

class Solution:
    def canPartition(self, nums) -> bool:
        if not nums:
            return False

        target = sum(nums)
        if target % 2 != 0:
            return False

        n = target // 2
        m = len(nums) 
        dp = [[False for _ in range(0, n + 1)] for _ in range(0, m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]] 
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n] 

print(Solution().canPartition([1,5,11,5]))
