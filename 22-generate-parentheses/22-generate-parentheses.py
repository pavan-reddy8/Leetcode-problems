class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =[]
        com =[]
        def backtrack(lp,rp):
            if  rp == n and lp == n:
                res.append("".join(com))
                return
            if lp < n: 
                com.append('(')
                backtrack(lp+1,rp)
                com.pop()
            if rp < lp:
                com .append(')')
                backtrack(lp,rp+1)
                com.pop()

        backtrack(0,0)
        return res

    
            
            
        