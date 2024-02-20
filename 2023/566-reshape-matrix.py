class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        def iter_matrix(mat):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    yield mat[i][j]

        imatrix = iter_matrix(mat)
        matrix = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                matrix[i][j] = next(imatrix) 
        return matrix

