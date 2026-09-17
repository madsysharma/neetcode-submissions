class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def bubbleUp(self, idx: int) -> None:
        parent = idx // 2
        while idx > 1 and self.heap[parent] > self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
            parent = idx // 2
    
    def bubbleDown(self, idx: int) -> None:
        child = 2 * idx
        while child < len(self.heap):
            if (child + 1) < len(self.heap) and self.heap[child] > self.heap[child + 1]:
                child += 1
            
            if self.heap[child] >= self.heap[idx]:
                break

            self.heap[child], self.heap[idx] = self.heap[idx], self.heap[child]
            idx = child
            child = 2 * idx

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.bubbleUp(len(self.heap) - 1)

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        elif len(self.heap) == 2:
            return self.heap.pop()
        else:
            root = self.heap[1]
            self.heap[1] = self.heap.pop()
            self.bubbleDown(1)
            return root

    def top(self) -> int:
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        for i in reversed(range(1, len(self.heap)//2 + 1)):
            self.bubbleDown(i)