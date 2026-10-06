import random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        while True:
            picked = random.choice(nums)
            if nums.count(picked) > (n // 2):
                return picked