class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = ct = 0
        for n in nums:
            if ct == 0:
                res = n
            
            ct = ct + 1 if n == res else ct - 1
        return res