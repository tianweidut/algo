class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        results = []
        def backtrack(state, choices):
            results.append(state.copy())

            record = set()
            for idx, c in enumerate(choices):
                if c in record:
                    continue

                record.add(c)
                state.append(c)
                backtrack(state, choices[idx+1:])
                state.pop()

        nums.sort()
        backtrack(state=[], choices=nums)
        return results
