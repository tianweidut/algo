class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        left, right = 0, int(math.sqrt(c)) + 1
        while left <= right:
            val = left * left + right * right
            if val == c:
                return True
            elif val < c:
                left += 1
            else:
                right -= 1

        return False
