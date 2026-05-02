import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            if i < len(nums)-1:
                result.append(math.prod(nums[:i]) * math.prod(nums[i+1:]))
            elif i == len(nums)-1:
                result.append(math.prod(nums[:i]))
        return result