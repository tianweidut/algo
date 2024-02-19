class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_nums = []

        sum_val = 0
        for n in nums:
            sum_val += n
            self.sum_nums.append(sum_val)

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_nums[right] - (0 if left <= 0 else self.sum_nums[left - 1])
