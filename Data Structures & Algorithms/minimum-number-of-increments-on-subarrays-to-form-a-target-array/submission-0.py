class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ct = target[0]
        for i in range(1, len(target)):
            ct += max(target[i] - target[i-1], 0)
        return ct
            
            