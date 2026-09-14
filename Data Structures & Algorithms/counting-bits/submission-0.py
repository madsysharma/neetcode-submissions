class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)

        for i in range(1, n+1):
            temp = i
            while temp != 0:
                output[i] += (temp & 1)
                temp = temp >> 1
        
        return output