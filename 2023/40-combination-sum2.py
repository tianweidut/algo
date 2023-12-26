class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(choices, state, remain):
            if remain == 0:
                results.append(state.copy())
                return

            record = set()
            for idx, c in enumerate(choices):
                if c > remain:
                    break
                if c in record:
                    continue
                else:
                    record.add(c)

                state.append(c)
                backtrack(choices=choices[idx + 1:], state=state, remain=remain - c)
                state.pop()
            
        candidates.sort()
        backtrack(choices=candidates, state=[], remain=target)
        return results
