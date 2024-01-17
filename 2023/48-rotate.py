class Solution:
    def rotate(self, matrix) -> None:
        if not matrix:
            return

        n = len(matrix)
        for i in range(0, n // 2 + 1):
            for j in range(i, n - i - 1):
                (
                    matrix[j][n - 1 - i],
                    matrix[n - 1 - i][n - 1 - j],
                    matrix[n - 1 - j][i],
                    matrix[i][j],
                ) = (
                    matrix[i][j],
                    matrix[j][n - 1 - i],
                    matrix[n - 1 - i][n - 1 - j],
                    matrix[n - 1 - j][i],
                ) 
