class Solution:
    def numDecodings(self, s: str) -> int:
        r = r2 = 0
        r1 = 1
        n = len(s)

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                r = 0
            else:
                r = r1
            
            if (i + 1) < n and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                r += r2
            
            r, r1, r2 = 0, r, r1
        
        return r1