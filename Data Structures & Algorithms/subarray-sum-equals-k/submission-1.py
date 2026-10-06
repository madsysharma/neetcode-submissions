class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result, curr_sum = 0, 0
        pref_sums = {0: 1}

        for n in nums:
            curr_sum += n
            diff = curr_sum - k
            result += pref_sums.get(diff, 0)

            pref_sums[curr_sum] = 1 + pref_sums.get(curr_sum, 0)

        return result