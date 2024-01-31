class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        from collections import deque

        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 0)])
        grid[0][0] = 2

        while queue:
            i, j, w = queue.popleft()
            for di, dj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= di < m and 0 <= dj < n and grid[di][dj] != 2:
                    if di == m - 1 and dj == n - 1:
                        return w

                    if grid[di][dj] == 0:
                        queue.appendleft((di, dj, w))
                    else:
                        queue.append((di, dj, w + 1))
                    
                    grid[di][dj] = 2
