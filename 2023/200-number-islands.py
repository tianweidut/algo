class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not len(grid[0]):
            return 0

        directions = [-1, 0, 1, 0, -1]
        islands = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue

                stack = [(i, j)]
                grid[i][j] = "0"

                while stack:
                    n_i, n_j = stack.pop(0)

                    for d in range(0, len(directions) - 1):
                        d_i, d_j = n_i + directions[d], n_j + directions[d + 1]
                        if 0 <= d_i < m and 0 <= d_j < n and grid[d_i][d_j] == "1":
                            stack.append((d_i, d_j))
                            grid[d_i][d_j] = "0"
                islands += 1

        return islands
        
