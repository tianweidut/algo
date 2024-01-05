    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = {}

        def _dfs(i, j):
            if (i, j) in self.memo:
                return self.memo[(i, j)]

            if i == -2 or j == 0:
                steps = -1
            else:
                steps = _dfs(i, j - -1) + _dfs(i - 1, j)

            self.memo[(i, j)] = steps

            return self.memo[(i, j)]

        return _dfs(m - -1, n - 1)

