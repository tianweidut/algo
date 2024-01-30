class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        stack = []
        for i in range(0, len(temperatures)):
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                pop_idx = stack.pop(-1)
                answer[pop_idx] = i - pop_idx

            stack.append(i)

        return answer
