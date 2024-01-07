class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            pre = 0
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    pre = max(dp[j], pre)
            dp[i] = pre + 1

        return max(dp)
