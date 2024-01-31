class MinStack:

    def __init__(self):
        self._normal_stack = []
        self._smaller_stack = []

    def push(self, val: int) -> None:
        self._normal_stack.append(val)
        if self._smaller_stack and self._smaller_stack[-1] < val:
            self._smaller_stack.append(self._smaller_stack[-1])
        else:
            self._smaller_stack.append(val)

    def pop(self) -> None:
        self._normal_stack.pop(-1)
        self._smaller_stack.pop(-1)

    def top(self) -> int:
        return self._normal_stack[-1]

    def getMin(self) -> int:
        return self._smaller_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
