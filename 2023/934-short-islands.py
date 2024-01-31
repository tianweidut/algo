class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        from collections import deque
        if not grid or not grid[0]:
            return -1

        self.directions = [-1, 0, 1, 0, -1]
        self.m, self.n = len(grid), len(grid[0])
        self.sides_queue = deque()

        def dfs(i, j):
            if grid[i][j] == 0:
                self.sides_queue.append((i, j))
                return

            grid[i][j] = 2
            for d in range(0, len(self.directions) - 1):
                di, dj = i + self.directions[d], j + self.directions[d + 1]
                if 0 <= di < self.m and 0 <= dj < self.n and grid[di][dj] != 2: 
                    dfs(di, dj)

        found = False
        for i in range(0, self.m):
            if found:
                break
            for j in range(0, self.n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
        levels = 0
        while self.sides_queue:
            levels += 1
            for _ in range(len(self.sides_queue)):
                i, j = self.sides_queue.popleft()
                grid[i][j] = 2

                for d in range(0, len(self.directions) - 1):
                    di, dj = i + self.directions[d], j + self.directions[d + 1]
                    if 0 <= di < self.m and 0 <= dj < self.n:
                        if grid[di][dj] == 1:
                            return levels
                        elif grid[di][dj] == 2:
                            continue
                        else:
                            self.sides_queue.append((di, dj))

        return -1

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        from collections import deque

        m, n = len(grid), len(grid[0])
        queue = deque()

        def bfs(i, j):
            queue.append((i, j, 0))
            grid[i][j] = 2

            while queue:
                ci, cj, levels = queue.popleft()

                for di, dj in ((ci + 1, cj), (ci - 1, cj), (ci, cj + 1), (ci, cj - 1)):
                    if di < 0 or di >= m or dj < 0 or dj >= n or grid[di][dj] == 2:
                        continue

                    if grid[di][dj] == 0:
                        queue.append((di, dj, levels + 1))
                    elif grid[di][dj] == 1:
                        if levels == 0:
                            queue.appendleft((di, dj, levels))
                        else:
                            return levels

                    grid[di][dj] = 2

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    return bfs(i, j)
