import math
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k==0 or len(nums)==0:
            return 0
        else:
            results = []
            buckets = [[] for x in range(10)]
            counts = {}
            for n in nums:
                b_idx = n%10 if n<=10 else int(n/(10**int(math.log(n, 10))))
                buckets[b_idx].append(n)
            for i in range(10):
                for j in buckets[i]:
                    counts[j] = buckets[i].count(j)
            k_freq = list(sorted(counts.values(), reverse = True))[:k]
            for key, val in counts.items():
                if val in k_freq:
                    results.append(key)
            return list(set(results))
            
            