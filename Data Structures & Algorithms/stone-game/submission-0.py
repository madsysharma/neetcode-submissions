class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if len(piles) == 2:
            return True
        
        l, r = 0, len(piles) - 1
        a, b = 0, 0
        while l < r:
            a += max(piles[l], piles[r])
            b += min(piles[l], piles[r])
            l += 1
            r -= 1
        
        return True if a > b else False