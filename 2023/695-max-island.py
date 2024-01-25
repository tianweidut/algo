class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        max_island = 0
        visited = {}

        def _dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0

            if grid[i][j] == 0:
                return 0

            if (i, j) in visited:
                return 0

            visited[(i, j)] = True
            val = 1 + _dfs(i - 1, j) + _dfs(i + 1, j) + _dfs(i, j - 1) + _dfs(i, j + 1)
            nonlocal max_island
            max_island = max(max_island, val)

            return val

        for i in range(m):
            for j in range(n):
                _dfs(i, j)

        return max_island
