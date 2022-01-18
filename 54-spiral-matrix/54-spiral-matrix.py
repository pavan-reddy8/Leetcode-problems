class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        l = 0 
        r = len(m[0])
        t = 0 
        b = len(m)
        res=[]

        while(l<r and t<b):
            print(res)
            for p in range(l,r):
                res.append(m[t][p])
            t +=1
            print(res,1)
            for q in range(t,b):
                res.append(m[q][r-1])  
            r -=1
            print(res,2)
            if not (l<r and t<b):
                break
            for p in range(r-1,l-1,-1):
                res.append(m[b-1][p])
            b-=1
            print(res,3)
            for q in range(b-1,t-1,-1):
                res.append(m[q][l])
            l+=1
            print(res,4)
        return res
            
            
            
        