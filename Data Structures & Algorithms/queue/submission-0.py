class Deque:
    
    def __init__(self):
        self.queue = []

    def isEmpty(self) -> bool:
        return (len(self.queue) == 0)

    def append(self, value: int) -> None:
        self.queue.append(value)

    def appendleft(self, value: int) -> None:
        self.queue.insert(0, value)

    def pop(self) -> int:
        return self.queue.pop() if not self.isEmpty() else -1

    def popleft(self) -> int:
        return self.queue.pop(0) if not self.isEmpty() else -1
