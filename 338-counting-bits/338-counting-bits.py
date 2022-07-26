class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            r = 0
            while i:
                r+=(i%2)
                i//=2
            res.append(r)
        return res
            