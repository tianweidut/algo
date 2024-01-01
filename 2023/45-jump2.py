class Solution:
    def jump(self, nums):
        farthest = 0
        end = 0
        jumps = 0
        for i in range(0, len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if end == i:
                jumps += 1
                end = farthest

        return jumps

    def jump2(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        jumps = 0
        idx = 0
        next_idx = idx

        while True:
            max_step = -1
            for i in range(0, nums[idx] + 1):
                if idx + i >= len(nums) - 1:
                    jumps += 1
                    return jumps

                if max_step < nums[idx + i] + i:
                    max_step = nums[idx + i] + i
                    next_idx = idx + i
                    print(f"next:{next_idx}, idx:{idx}")

            print(f"--> next:{next_idx}, idx:{idx}")
            if idx == next_idx:
                return 0

            idx = next_idx
            jumps += 1

        return jumps
