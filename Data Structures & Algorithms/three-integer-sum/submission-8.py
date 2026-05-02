class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            results = []
            nums.sort()
            for i, e in enumerate(nums):
                if e > 0:
                    break
                if i > 0 and e == nums[i - 1]:
                    continue
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    tot = e + nums[left] + nums[right]
                    if tot > 0:
                        right -= 1
                    elif tot < 0:
                        left += 1
                    else:
                        results.append([e, nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
            return results