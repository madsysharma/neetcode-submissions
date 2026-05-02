class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_table = {}
        for n in nums:
            if n not in count_table.keys():
                count_table[n] = 1
            else:
                print("Duplicate found")
                return True
        return False
         