class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res =[]
        com =[]
        def backtrack(s,p):
            if len(com) > k or s > n:
                return
            if len(com) == k and s == n:
                res.append(com.copy())
                return
            for i in range(p,10):
                com.append(i)
                backtrack(s+i,i+1)
                com.pop()
                
        backtrack(0,1)
        return res
        
        