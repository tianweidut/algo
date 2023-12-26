class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []

        def backtrack(remain, state, start):
            if remain == 0:
                results.append(state.copy())
                return

            # 去掉之前处理过的序列，避免重复，所以引入 start 参数
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                state.append(candidates[i])
                backtrack(remain - candidates[i], state,i)
                state.pop()

        backtrack(target, [], 0)
        return results
