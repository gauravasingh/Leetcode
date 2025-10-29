class MinStack:

    def __init__(self):
        self.stack = []      # normal stack
        self.min_stack = []  # stack to track current minimums

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the new min (min of current val and previous min)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
