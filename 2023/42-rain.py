class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) <= 2:
            return 0
        
        n = len(height)

        lmax = 0
        left_view = [0] * n
        for i in range(0, n):
            lmax = max(lmax, height[i])
            left_view[i] = lmax

        rmax = 0
        right_view = [0] * n
        for i in range(n-1, -1, -1):
            rmax = max(rmax, height[i])
            right_view[i] = rmax

        dp = [0] * n
        for i in range(0, n):
            dp[i] = min(left_view[i], right_view[i]) - height[i]

        return sum(dp)

