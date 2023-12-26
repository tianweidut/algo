class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        results = []
        def backtrack(choices, state):
            results.append(state.copy())

            for idx, c in enumerate(choices):
                state.append(c)
                backtrack(choices[idx + 1:], state)
                state.pop()

        backtrack(choices=nums, state=[])
        return results
