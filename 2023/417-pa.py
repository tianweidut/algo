class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        reach_p = [[False for _ in range(n)] for _ in range(m)]
        reach_a = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j, reach):
            if reach[i][j]:
                return

            reach[i][j] = True
            directions = [-1, 0, 1, 0, -1]
            for d in range(0, len(directions) - 1):
                d_i, d_j = i + directions[d], j + directions[d + 1]
                if 0 <= d_i < m and 0 <= d_j < n and heights[i][j] <= heights[d_i][d_j]:
                    dfs(d_i, d_j, reach)

        for i in range(m):
            dfs(i, 0, reach_p)
            dfs(i, n - 1, reach_a)

        for i in range(n):
            dfs(0, i, reach_p)
            dfs(m - 1, i, reach_a)

        targets = []
        for i in range(m):
            for j in range(n):
                if reach_a[i][j] and reach_p[i][j]:
                    targets.append((i, j))

        return targets
