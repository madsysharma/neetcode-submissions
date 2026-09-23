class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sup = []

        def dfs(idx: int, curr: List[int], nums: List[int], res: List[List[int]]):
            if idx == len(nums):
                res.append(curr[:])
                return
            
            curr.append(nums[idx])
            dfs(idx + 1, curr, nums, res)
            curr.pop()
            dfs(idx + 1, curr, nums, res)
        
        dfs(0, [], nums, sup)
        return sup