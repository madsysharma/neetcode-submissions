from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_counts = Counter(nums)
        n = len(nums)
        for k, v in num_counts.items():
            if num_counts[k] > (n // 2):
                return k