class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            n = len(nums)
            tab = [0] * n
            tab[n - 1] = nums[n - 1]
            tab[n - 2] = nums[n - 2]

            for i in range(n - 3, -1, -1):
                for j in range(i + 2, n):
                    tab[i] = max(tab[i], nums[i] + tab[j])
            
            return max(tab)