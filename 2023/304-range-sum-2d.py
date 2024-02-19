class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            sum_val = 0
            for j in range(len(matrix[0])):
                sum_val += matrix[i][j]
                self.sum_matrix[i][j] = sum_val 

        for j in range(len(matrix[0])):
            sum_val = 0
            for i in range(len(matrix)):
                sum_val += self.sum_matrix[i][j]
                self.sum_matrix[i][j] = sum_val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s1 = self.sum_matrix[row2][col2]

        s2 = self.sum_matrix[row1 - 1][col1 - 1] if row1 != 0 and col1 != 0 else 0  
        s3 = self.sum_matrix[row2][col1 - 1] if col1 != 0 else 0
        s4 = self.sum_matrix[row1 - 1][col2] if row1 != 0 else 0

        return s1 - s3 - s4 + s2
