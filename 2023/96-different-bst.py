class Solution:
    def numTrees(self, n: int) -> int:
        self.memo = {}
        nums = list(range(1, n+1))
        return self._travel(nums)

    def _travel(self, nums) -> int:
        if len(nums) <= 1: return 1

        key = (nums[0], nums[-1])
        if key in self.memo:
            return self.memo[key]

        cnt = 0
        for idx in range(0, len(nums)):
            left_cnt = self._travel(nums[:idx])
            right_cnt = self._travel(nums[idx+1:])
            cnt += left_cnt * right_cnt

        self.memo[key] = cnt
        return cnt

if __name__ == "__main__":
    print(Solution().numTrees(5))
    print(Solution().numTrees(1))
    print(Solution().numTrees(3))
