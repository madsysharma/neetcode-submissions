class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        combos = {}
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff not in combos:
                combos[nums[i]] = i
            else:
                return [combos[diff], i]