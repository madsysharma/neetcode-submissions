class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        pt, l = 0, 0
        n = len(s)
        tab = [[False] * n for x in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i) <= 2 or tab[i + 1][j - 1]):
                    tab[i][j] = True
                    if l < (j - i + 1):
                        pt = i
                        l = j - i + 1
        
        return s[pt: pt + l]