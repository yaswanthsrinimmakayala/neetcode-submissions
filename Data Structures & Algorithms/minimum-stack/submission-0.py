class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack  = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val, self.minStack[-1] if self.minStack else val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
