class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        res = []
        pas,atl = set(),set()
        
        def dfs(r,c,visited,prev):

            if (r,c) in visited or r < 0 or c < 0 or r == row or c == col or prev > heights[r][c]:
                return
            visited.add((r,c))
            for (a,b) in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(r+a,c+b,visited,heights[r][c])
            
        for c in range(col):
            dfs(0,c,pas,heights[0][c])
            dfs(row-1,c,atl,heights[row-1][c])
        
        for r in range(row):
            dfs(r,0,pas,heights[r][0])
            dfs(r,col-1,atl,heights[r][col-1])
            
        print (pas,atl)
        for r in range(row):
            for c in range(col):
                if (r,c) in pas and (r,c) in atl:
                    res.append((r,c))
                    
        return res