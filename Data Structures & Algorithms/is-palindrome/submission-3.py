import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        else:
            new_str = s.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
            print(new_str)
            left = 0
            right = len(new_str) - 1
            while left < right:
                if new_str[left] == new_str[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
