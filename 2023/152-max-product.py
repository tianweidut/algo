class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [nums[0]] + [0] * (n-1)
        dp_min = [nums[0]] + [0] * (n-1)

        for i in range(1, n):
            choice = (dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
            dp_max[i] = max(choice)
            dp_min[i] = min(choice)

        return max(dp_max)
