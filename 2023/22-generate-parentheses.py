class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def dfs(start, record, left, right):
            if start == 2 * n:
                return

            if left < n:
                record += "("
                if start == 2 * n - 1:
                    results.append(record)
                dfs(start + 1, record, left + 1, right)
                record = record[:-1]

            if right < left and right < n:
                record += ")"
                if start == 2 * n - 1:
                    results.append(record)
                dfs(start + 1, record, left, right + 1)
                record = record[:-1]

        dfs(0, "", 0, 0)
        return results
