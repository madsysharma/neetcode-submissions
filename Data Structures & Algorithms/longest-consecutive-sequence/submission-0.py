class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      num_set = set(nums)
      lcs = 0
      for n in num_set:
        if (n-1) not in num_set:
            length = 1
            while (n+length) in num_set:
                length += 1
            lcs = max(length, lcs)
      return lcs
      