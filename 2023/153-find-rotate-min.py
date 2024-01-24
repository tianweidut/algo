class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] <= nums[mid] <= nums[right]:
                return nums[left]
            elif nums[left] >= nums[mid] >= nums[right]:
                return nums[right]
            elif nums[left] < nums[mid] > nums[right]:
                left = mid + 1
            else:
                if mid > 0 and nums[mid] < nums[mid - 1]:
                    return nums[mid]
                else:
                    right = mid - 1
