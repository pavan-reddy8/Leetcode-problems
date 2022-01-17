class Solution:
    def construct2DArray(self, o: List[int], m: int, n: int) -> List[List[int]]:
        res=[]
        oi=0
        if m*n!=len(o):
            return res
        for i in range(m):
            l=[]
            j=0
            while j<n and oi<len(o):
                l.append(o[oi])
                j+=1
                oi+=1
            res.append(l)
        return res
        
        