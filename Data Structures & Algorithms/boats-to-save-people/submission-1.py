class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Key component of solution: counting sort
        # Steps: get max weight of array -> create count array of size (max_w + 1) ->
        # Count freq of each weight -> reconstruct sorted array by looping through count array
        # Use 2 ptrs, l and r (0 and end): while l<=r, heaviest person takes a boat
        # If the lightest person fits with them, include them too
        max_w = max(people)
        count = [0] * (max_w + 1)
        for p in people:
            count[p] += 1
        
        ptr, i = 0, 1
        n = len(people)
        while ptr < n:
            while count[i] == 0:
                i += 1
            people[ptr] = i
            count[i] -= 1
            ptr += 1
        
        l, r = 0, n - 1
        res = 0
        while l <= r:
            diff = limit - people[r]
            r -= 1
            res += 1
            if l <= r and diff >= people[l]:
                l += 1
        return res