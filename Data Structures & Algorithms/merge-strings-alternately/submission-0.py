class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        idx = 0
        if len(word1) == 0:
            return word2
        elif len(word2) == 0:
            return word1
        elif len(word1) == len(word2):
            n = len(word1)
            while idx < n:
                res += word1[idx] + word2[idx]
                idx += 1
            return res
        else:
            n = min(len(word1), len(word2))
            while idx < n:
                res += word1[idx] + word2[idx]
                idx += 1
            
            if idx < len(word1):
                res += word1[idx:]
            
            if idx < len(word2):
                res += word2[idx:]

        return res