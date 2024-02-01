class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        # edge dfs
        edges = [[False for _ in range(n)] for _ in range(m)]
        def dfs(i, j):
            if board[i][j] == "X":
                return

            edges[i][j] = True
            for di, dj in ((i + 1, j), (i-1, j), (i, j + 1), (i, j - 1)):
                if 0 <= di < m and 0 <= dj < n and board[di][dj] == "O" and not edges[di][dj]:
                    dfs(di, dj)  

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        # mark o -> x
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not edges[i][j]:
                    board[i][j] = "X"
