class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def shell_sort(nums, n):
            gap = n // 2
            while gap >= 1:
                for i in range(gap, n):
                    temp = nums[i]
                    j = i - gap
                    while j >= 0 and nums[j] > temp:
                        nums[j + gap] = nums[j]
                        j -= gap
                    nums[j + gap] = temp
                gap = gap // 2
            
        n = len(nums)
        if n == 1:
            return nums
        else:
            shell_sort(nums, n)
            return nums