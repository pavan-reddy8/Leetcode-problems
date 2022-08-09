class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        Rowlen = len(h)
        Collen = len(h[0])
        p =[]
        vp = set()
        a=[]
        va = set()
 
        for r in range(Rowlen):
            p.append((r,0))
            a.append((r,Collen-1))
        for c in range(Collen):
            p.append((0,c))
            a.append((Rowlen-1,c))
            
        def dfs(r,c,visited):
            visited.add((r,c))
            moves = [(0,1),(0,-1),(1,0),(-1,0)]
            for move in moves:
                row = r + move[0]
                col = c + move[1]
                if 0 <=row < Rowlen and 0 <=col < Collen and (row,col) not in visited and  h[r][c] <= h[row][col]:
                    dfs(row,col,visited)
        for r,c in p:
            dfs(r,c,vp)
        for r,c in a:
            dfs(r,c,va)

        res = vp & va
        print(res)
        return res
                
                
                
        