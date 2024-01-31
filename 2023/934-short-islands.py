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
