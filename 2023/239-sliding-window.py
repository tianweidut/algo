class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        max_values = []
        
        if k <= 0 or not nums:
            return []

        if k > len(nums):
            return [max(nums)]

        queue = deque()
        # init k window
        for i in range(0, k):
            while queue:
                if queue[-1] < nums[i]:
                    queue.pop()
                else:
                    break
            queue.append(nums[i])

        max_values.append(queue[0])
        
        # sliding k window
        for i in range(k, len(nums)):
            if nums[i-k] == queue[0]:
                queue.popleft()

            while queue:
                if queue[-1] < nums[i]:
                    queue.pop()
                else:
                    break
            queue.append(nums[i])

            max_values.append(queue[0])

        return max_values
