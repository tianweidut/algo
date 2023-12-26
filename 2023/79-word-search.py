class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_row = len(board)
        board_col = len(board[0])

        self.memo = {}

        def backtrack(row, col, state, word):
            if word == "":
                return True

            if row < 0 or col < 0 or row >= board_row or col >= board_col:
                return False

            if state[row][col] or board[row][col] != word[0]:
                return False


            state[row][col] = True
            word = word[1:]
            r = (
                backtrack(row, col + 1, state, word) or
                backtrack(row, col - 1, state, word) or
                backtrack(row - 1, col, state, word) or
                backtrack(row + 1, col, state, word)
            )
            state[row][col] = False
            return r
        
        for row in range(0, board_row):
            for col in range(0, board_col):
                state = [[False for _ in range(board_col)] for _ in range(board_row)]
                if backtrack(row, col, state, word):
                    return True

        return False
