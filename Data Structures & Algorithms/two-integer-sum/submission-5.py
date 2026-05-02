class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       pair_dict={}
       for i, n in enumerate(nums):
        d = target - n
        if d in pair_dict:
            return [pair_dict[d],i]
        else:
            pair_dict[n] = i
        
