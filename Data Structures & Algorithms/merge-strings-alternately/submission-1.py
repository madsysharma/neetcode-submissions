class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == 0 and len(word2) > 0:
            return word2
        elif len(word2) == 0 and len(word1) > 0:
            return word1
        else:
            result = ""
            m, n = len(word1), len(word2)
            i, j = 0, 0

            while i < m and j < n:
                result += word1[i] + word2[j]
                i += 1
                j += 1

            if i == m:
                result += word2[j:]
            
            if j == n:
                result += word1[i:]
            
            return result