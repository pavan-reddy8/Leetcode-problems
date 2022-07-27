class Solution:
    def reverseBits(self, n: int) -> int:
        i = 31
        res = 0
        while i >= 0 :
            bit = n & 1
            bit = bit << i
            res = res | bit
            n = n >> 1
            i -= 1
            # print (bin(res))
        return res