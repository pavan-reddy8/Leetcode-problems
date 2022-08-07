class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = [0]
        q = []
        fres = 0
        def bfs(r,c):
            q.append((r,c))
            while q:
                r,c = q.pop(0)
                moves = [(1,0),(-1,0),(0,1),(0,-1)]
                for move in moves:
                    row = r+move[0]
                    col = c+move[1]
                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row,col) not in visited and grid[row][col] == 1:
                        visited.add((row,col))
                        q.append((row,col))
                        res[0] += 1
                        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] ==1 :
                    visited.add((r,c))
                    res[0] +=1
                    bfs(r,c)
                    fres= max(fres,res[0])
                    
                res[0] = 0
        return fres
        