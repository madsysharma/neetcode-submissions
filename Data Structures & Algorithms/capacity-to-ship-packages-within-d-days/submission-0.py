class Solution:
    def requiredDays(self, weights, capacity):
        days_needed = 1
        current_load = 0
        for w in weights:
            if current_load + w > capacity:
                days_needed += 1
                current_load = w
            else:
                current_load += w
        return days_needed
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        res = high
        while low <= high:
            mid = (low + high) // 2
            fast_enough = self.requiredDays(weights, mid) <= days

            if fast_enough:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res