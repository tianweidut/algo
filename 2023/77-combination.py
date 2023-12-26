class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < 1 or k < 0:
            return []

        results = []
        def backtrack(state, choices):
            if len(state) == k:
                results.append(state.copy())
                return

            for idx, c in enumerate(choices):
                state.append(c)
                backtrack(state, choices[idx+1:])
                state.pop()

        backtrack(state=[], choices=list(range(1, n+1)))
        return results

