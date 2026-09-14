class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 1
        n = len(nums)
        for end in range(1, n):
            if nums[end] != nums[end - 1]:
                nums[start] = nums[end]
                start += 1
        return start