class Solution:
    def getAbsDifference(self, subarray):
        return abs(max(subarray) - min(subarray))
    
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_len = 0

        '''for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                diff = self.getAbsDifference(nums[i:j])
                if diff <= limit:
                    max_len = max(max_len, len(nums[i:j]))'''

        l, r = 0, 0
        while r < len(nums) and l < len(nums):
            diff = self.getAbsDifference(nums[l:r+1])
            if diff > limit:
                l += 1
            else:
                max_len = max(max_len, len(nums[l:r+1]))
            r += 1
        
        return max_len