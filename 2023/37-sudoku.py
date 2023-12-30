class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_len = len(board)
        col_len = len(board[0])

        def backtrack(row, col):
            if col == col_len:
                return backtrack(row + 1, 0)
            
            if row == row_len:
                return True

            if board[row][col] != ".":
                return backtrack(row, col + 1)

            for i in range(1, 10):
                ch = str(i)
                if not self.is_valid(board, row, col, ch):
                    continue

                board[row][col] = ch
                if backtrack(row, col + 1):
                    return True
                board[row][col] = "."

            return False

        backtrack(0, 0)
        return

    def is_valid(self, board, row, col, ch):
        for idx in range(0, len(board)):
            if ch == board[idx][col]:
                return False

        for idx in range(0, len(board[0])):
            if ch == board[row][idx]:
                return False

        grid_row = (row // 3) * 3
        grid_col = (col // 3) * 3
        for gr in range(grid_row,  grid_row + 3):
            for gc in range(grid_col, grid_col + 3):
                if board[gr][gc] == ch:
                    return False

        return True
        
