class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1) 
        for i in range(n+1):
            r = i%2 
            j = i//2
            r+=res[j]
            res[i] = r
        return res
            