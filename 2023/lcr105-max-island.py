class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        directions = [-1, 0, 1, 0, -1]
        m, n = len(grid), len(grid[0])
        max_islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                stack = [(i, j)]
                local_islands = 1
                grid[i][j] = 0

                while stack:
                    l_i, l_j = stack.pop(0)
                    for d in range(0, len(directions) - 1):
                        n_i, n_j = l_i + directions[d], l_j + directions[d + 1]
                        if 0 <= n_i < m and 0 <= n_j < n and grid[n_i][n_j] == 1:
                            stack.append((n_i, n_j))
                            grid[n_i][n_j] = 0
                            local_islands += 1

                max_islands = max(max_islands, local_islands)

        return max_islands
