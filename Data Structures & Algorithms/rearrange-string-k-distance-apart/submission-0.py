import heapq
from collections import Counter, deque

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s
        
        char_counts = Counter(s)
        max_heap = [(-f, c) for c, f in char_counts.items()]
        heapq.heapify(max_heap)

        wait_queue = deque()
        result = []

        while max_heap:
            f, c = heapq.heappop(max_heap)
            result.append(c)
            wait_queue.append((f+1, c))

            if len(wait_queue) == k:
                f, c = wait_queue.popleft()
                if f < 0:
                    heapq.heappush(max_heap, (f, c))

        return "".join(result) if len(result) == len(s) else ""