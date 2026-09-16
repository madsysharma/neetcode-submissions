class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        pref = 0
        suff = 0

        for i in range(n):
            pref = nums[i] * (pref or 1)
            suff = nums[n - i - 1] * (suff or 1)
            res = max(res, max(pref, suff))
        
        return res