class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        self.memo = {}
        def backtrack(start, remain):
            if remain == 0:
                return 1

            cnt = 0
            for idx in range(start, len(nums)):
                if nums[idx] > remain:
                    break

                r = remain - nums[idx]
                if (start, r) not in self.memo:
                    self.memo[(start, r)] = backtrack(start=start, remain=r)
                 
                cnt += self.memo[(start, r)]
            return cnt

        nums.sort()
        return backtrack(start=0, remain=target)
