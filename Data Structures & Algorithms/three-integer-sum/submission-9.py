class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        else:
            nums.sort()
            triplets = []
            n = len(nums)
            for i in range(n):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                diff = -(nums[i])
                j = i + 1
                k = n - 1
                while j < k:
                    current_sum = nums[j] + nums[k]
                    if current_sum < diff:
                        j += 1
                    elif current_sum > diff:
                        k -= 1
                    else:
                        triplets.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            return triplets