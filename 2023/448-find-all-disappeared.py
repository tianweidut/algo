class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        targets = [0] * (len(nums) + 1)
        for n in nums:
            targets[n] = 1

        return [idx for idx, n in enumerate(targets[1:], 1) if n == 0]
