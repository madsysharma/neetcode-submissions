class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                sub1 = s[:r] + s[r+1:]
                sub2 = s[:l] + s[l+1:]
                if sub1[::-1] != sub1 and sub2[::-1] != sub2:
                    return False
                else:
                    return True
            l += 1
            r -= 1
        return True