class Solution:
    def exist(self, b: List[List[str]], word: str) -> bool:
        row = len(b)
        col = len(b[0])
        path = set() 
        def dfs(i,j,s):
      
            if s==len(word):
                return True
            if i < 0 or i >= row or j < 0 or j >= col or word[s] != b[i][j] or (i,j) in path:
                return False
            path.add((i,j))
            if dfs(i,j+1,s+1) or dfs(i+1,j,s+1) or dfs(i,j-1,s+1) or dfs(i-1,j,s+1):
                return True
            path.remove((i,j))
            return False
        
        for i in range(row):
            for j in range(col):
                path.clear()
                if dfs(i,j,0):
                    return True
                

                
            
        