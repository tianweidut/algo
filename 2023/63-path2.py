class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        self.memo = {}

        for i in range(0, m):
            if obstacleGrid[i][0] == 1:
                for j in range(i, m):
                    obstacleGrid[j][0] = 1
                break

        for i in range(0, n):
            if obstacleGrid[0][i] == 1:
                for j in range(i, n):
                    obstacleGrid[0][j] = 1
                break

        def _dfs(i, j):
            if (i, j) in self.memo:
                return self.memo[(i, j)]

            if i == 0 or j == 0:
                steps = 1 if obstacleGrid[i][j] == 0 else 0
            else:
                steps = (
                    _dfs(i - 1, j) + _dfs(i, j - 1) if obstacleGrid[i][j] == 0 else 0
                )

            self.memo[(i, j)] = steps
            return steps

        return _dfs(m - 1, n - 1)
