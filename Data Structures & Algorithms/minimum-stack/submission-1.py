class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        new_min = 0
        if len(self.st) == 0:
            new_min = val
        else:
            new_min = min(val, self.st[-1][1])
        self.st.append((val, new_min))

    def pop(self) -> None:
        self.st.pop()
    
    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]