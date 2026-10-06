from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        picked_fruits = Counter()
        n = len(fruits)
        l = 0
        max_num = 0
        for r in range(n):
            picked_fruits[fruits[r]] += 1
            while len(picked_fruits) > 2:
                picked_fruits[fruits[l]] -= 1
                if picked_fruits[fruits[l]] == 0:
                    del picked_fruits[fruits[l]]
                l += 1
            max_num = max(max_num, r - l + 1)
        return max_num
