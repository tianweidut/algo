class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid] >= nums[left]:
                    if target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    if target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1
