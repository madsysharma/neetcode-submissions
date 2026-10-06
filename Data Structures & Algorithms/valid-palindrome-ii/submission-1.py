class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = ("".join([c for c in s if c.isalnum])).lower()
        print(s)
        l, r = 0, len(s) - 1
        result = True
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                c1, c2 = s[l], s[r]
                n1 = s[:l] + s[l+1:]
                n2 = s[:r] + s[r+1:]
                print(n1)
                print(n2)
                if n1[::-1] == n1 or n2[::-1] == n2:
                    return True
                elif n1[::-1] != n1 and n2[::-1] != n2:
                    return False
                else:
                    l += 1
                    r -= 1
                    result = False
        return result