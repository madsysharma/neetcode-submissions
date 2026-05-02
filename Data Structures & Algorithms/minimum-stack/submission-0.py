class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimums)>0:
            self.minimums.append(min(val, self.minimums[-1]))
        else:
            self.minimums.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()


    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("Empty!")
            return -1

    def getMin(self) -> int:
        if len(self.minimums) > 0:
            return self.minimums[-1]
        else:
            print("Empty!")
            return -1
