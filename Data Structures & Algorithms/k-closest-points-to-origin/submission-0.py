import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for i, p in enumerate(points):
            x, y = p[0], p[1]
            dist = ((x ** 2) + (y ** 2)) ** 0.5
            min_heap.append((dist, x, y))
        
        heapq.heapify(min_heap)
        results = []
        for i in range(k):
            d, x, y = heapq.heappop(min_heap)
            results.append([x,y])
        
        return results