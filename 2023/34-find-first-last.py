class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        l_bound = self.lower(nums, target)
        u_bound = self.upper(nums, target)
        if l_bound <= u_bound < len(nums) and nums[l_bound] == nums[u_bound] == target:
            return [l_bound, u_bound]
        else:
            return [-1, -1]

    def upper(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return right

    def lower(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
