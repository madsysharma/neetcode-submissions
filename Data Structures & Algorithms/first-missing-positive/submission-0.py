class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Key idea: use the array itself as a hash map
        # Flag = sign of the number
        # If arr[i] < 0 -> i + 1 exists in arr. But arr may already have nums <= 0.
        # Thus, these are the steps:
        # Convert all non-positive elements to 0 -> for each v in range [1,n], mark elem at index v-1 as negative -> if it's already 0, use special marker -(n+1) to indicate its presence.
        # Result: first non-negative index

        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
            
        for i in range(n):
            v = abs(nums[i])
            if v in range(1, n+1):
                if nums[v - 1] > 0:
                    nums[v - 1] *= -1
                elif nums[v - 1] == 0:
                    nums[v - 1] = -1 * (n + 1)
        
        for i in range(1, n+1):
            if nums[i-1] >= 0:
                return i
        
        return n + 1