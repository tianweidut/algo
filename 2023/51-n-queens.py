class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []

        results = []
        def backtrack(state, row):
            if row == n:
                results.append(state.copy())
                return

            for col in range(0, n):
                new_row = self.gen_row(col, n)
                if not self.is_valid(new_row, state):
                    continue

                state.append(new_row)
                backtrack(state, row + 1)
                state.pop()

        backtrack(state=[], row=0)
        return results

    def gen_row(self, idx, n):
        s = ["." for _ in range(0, n)]
        s[idx] = "Q"
        return "".join(s)

    def is_valid(self, new_row, state):
        # check col
        row = len(state)
        col = new_row.find("Q")

        for c_row, c_state in enumerate(state):
            # check col
            if c_state[col] == "Q":
                return False

            # check up-left and right-left
            c_col = c_state.find("Q")
            if abs(c_row - row) == abs(c_col - col):
                return False

        return True
