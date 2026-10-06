class MyQueue:

    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        self.st.insert(0, x)

    def pop(self) -> int:
        if len(self.st) > 0:
            v = self.st.pop()
            return v
        else:
            return -1

    def peek(self) -> int:
        return self.st[-1]

    def empty(self) -> bool:
        return (self.st is None or len(self.st) == 0)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()