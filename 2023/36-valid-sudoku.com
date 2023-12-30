class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for idx in range(0, len(board)):
            record = set()
            for n in board[idx]:
                if n != '.' and n in record:
                    return False
                else:
                    record.add(n)

        # check col
        for j in range(0, len(board[0])):
            record = set()
            for i in range(0, len(board)):
                if board[i][j] != '.' and board[i][j] in record:
                    return False
                else:
                    record.add(board[i][j])

        # check grid
        for label in range(0, 9):
            row = (label // 3) * 3
            col = (label % 3) * 3

            record = set()
            for i in range(0, 3):
                for j in range(0, 3):
                    val = board[row + i][col + j]
                    if val != "." and val in record:
                        return False
                    else:
                        record.add(val)
        
        return True
