class MyQueue:

    def __init__(self):
        self.stack = []
        self.reversed_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self._transfer_to_reverse()
        return self.reversed_stack.pop()

    def peek(self) -> int:
        self._transfer_to_reverse()
        return self.reversed_stack[-1]

    def empty(self) -> bool:
        return not self.stack and not self.reversed_stack

    def _transfer_to_reverse(self):
        if not self.reversed_stack:
            while self.stack:
                self.reversed_stack.append(self.stack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()