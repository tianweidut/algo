class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 1
                elif nums[mid] == nums[mid - 1]:
                    right = mid - 1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid + 1]:
                    right = mid - 1
                elif nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    return nums[mid]

        return nums[left]
