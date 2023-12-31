class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        idx = 0
        while idx < len(nums):
            next_idx = idx
            max_step = -1
            for i in range(0, nums[idx] + 1):
                if idx + i >= len(nums) - 1:
                    return True

                if nums[idx + i] + i > max_step:
                    max_step = nums[idx + i] + i
                    next_idx = idx + i
            
            if next_idx == idx:
                return False

            idx = next_idx

        return True
