class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        directions = [-1, 0, 1, 0, -1]
        perimeter = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or grid[i][j] == 2:
                    continue

                stack = [(i, j)]
                grid[i][j] = 2

                while stack:
                    p_i, p_j = stack.pop(0)

                    for d in range(0, len(directions) - 1):
                        d_i, d_j = p_i + directions[d], p_j + directions[d + 1]

                        if (
                            d_i < 0
                            or d_i >= m
                            or d_j < 0
                            or d_j >= n
                            or grid[d_i][d_j] == 0
                        ):
                            perimeter += 1
                            continue

                        if grid[d_i][d_j] == 1:
                            stack.append((d_i, d_j))
                            grid[d_i][d_j] = 2

        return perimeter
