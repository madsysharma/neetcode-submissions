from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_counts = Counter(s)
        t_char_counts = Counter(t)

        if s_char_counts == t_char_counts:
            return True
        else:
            return False