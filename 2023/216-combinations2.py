class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k < 0 or n < 0:
            return []

        results = []
        def backtrack(state, choices, remain):
            if len(state) == k and remain == 0:
                results.append(state.copy())
                return
            
            if remain <= 0 or len(state) >= k:
                return

            for idx, c in enumerate(choices):
                state.append(c)
                backtrack(state=state, choices=choices[idx+1:], remain=remain - c)
                state.pop()

        backtrack(state=[], choices=list(range(1, 10)), remain=n)
        return results
