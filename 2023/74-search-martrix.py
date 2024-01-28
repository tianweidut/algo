class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = l + (r - l) // 2
            val = matrix[mid // n][ mid % n] 
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        def search(nums):
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if target == nums[mid]:
                    return True
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        i = 0
        while i < m:
            val = matrix[i][n-1]
            if val == target:
                return True
            elif val > target:
                return search(matrix[i])
            else:
                i += 1

        return False
            
