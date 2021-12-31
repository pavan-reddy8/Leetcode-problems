class Solution:
    def combinationSum(self, c: List[int], t: int) -> List[List[int]]:
        res =[]
        def dfs(i,cur,total):
            if total == t:
                res.append(cur.copy())
                return
            if i >= len(c) or total > t:
                return
            
            cur.append(c[i])
      
            dfs(i,cur,total +c[i])
            cur.pop()
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return res