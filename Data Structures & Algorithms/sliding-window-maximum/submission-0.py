class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==0 or k==0:
            return 0
        else:
            results = []
            start = 0
            while True:
                results.append(max(nums[start:start+k]))
                if start+k>=len(nums):
                    break
                start += 1
            return results
        