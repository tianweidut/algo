class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        def dfs(start, state):
            if start < 0 or start >= len(arr):
                return False

            if start in state:
                return False

            if arr[start] == 0:
                return True

            state[start] = True
            flag = dfs(start + arr[start], state) or dfs(start - arr[start], state)
            state[start] = False
            return flag

        return dfs(start, {})
