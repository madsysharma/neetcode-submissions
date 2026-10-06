class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                return True
        return False