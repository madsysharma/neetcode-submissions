class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        arr = list(set(nums))
        arr.sort()
        max_len = 0
        l = 0
        n = len(arr)
        for r in range(n):
            if r > 0 and arr[r] != arr[r - 1] + 1:
                l = r
            max_len = max(max_len, r - l + 1)
        return max_len