import math
class Solution:
    def hoursRequired(self, piles, speed):
        return sum(math.ceil(p / speed) for p in piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        while low <= high:
            mid = (low + high) // 2
            fast_enough = (self.hoursRequired(piles, mid) <= h)

            if fast_enough:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res