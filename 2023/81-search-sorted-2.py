class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    return self.search(nums[0:mid], target) or self.search(
                        nums[mid + 1 :], target
                    )
            else:
                if nums[mid] < nums[right]:
                    right = mid - 1
                else:
                    return self.search(nums[0:mid], target) or self.search(
                        nums[mid + 1 :], target
                    )

        return False
