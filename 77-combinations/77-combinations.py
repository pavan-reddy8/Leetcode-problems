class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        per =[]
        flag =[False]*n
        def backtrack(start):
            if len(per) == k:
                c = per.copy()
                if c not in res:
                    res.append(c)
                return
            for i in range(start,n+1):
                    per.append(i)
                    backtrack(start+1)
                    per.pop()
                    start+=1
        backtrack(1)
        return res