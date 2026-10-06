# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while True:
            a = l + (r - l)//3
            b = r - (r - l)//3
            if guess(a) == 0:
                return a
            if guess(b) == 0:
                return b

            if guess(a) + guess(b) == 0:
                l = a + 1
                r = b - 1
            elif guess(a) == -1:
                r = a - 1
            else:
                l = b + 1
                