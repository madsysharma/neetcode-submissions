class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        tab = [[False] * n for x in range(n)]
        count = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or tab[i+1][j-1]):
                    tab[i][j] = True
                    count += 1
        
        return count