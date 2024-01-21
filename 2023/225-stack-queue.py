class MyStack:

    def __init__(self):
        self.primary = []
        self.second = []

    def push(self, x: int) -> None:
        while self.primary:
            self.second.append(self.primary.pop(0))

        self.primary.append(x)
        while self.second:
            self.primary.append(self.second.pop(0))

    def pop(self) -> int:
        return self.primary.pop(0)

    def top(self) -> int:
        return self.primary[0]

    def empty(self) -> bool:
        return len(self.primary) == 0
