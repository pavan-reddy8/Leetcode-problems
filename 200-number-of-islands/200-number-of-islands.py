class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set(())
        res = 0
        q = []
        def bfs(r,c):

            q.append((r,c))
            visit.add((r,c))
            while q:
            
                curr, curc = q.pop(0)
                moves = [(0,1),(0,-1),(1,0),(-1,0)]
                for move in moves:
                    row = curr + move[0]
                    col = curc + move[1]
                    if  (row,col) not in visit and 0 <= row < len(grid) and 0 <= col <len(grid[0]) and grid[row][col] == '1':
                        q.append((row,col))
                        visit.add((row,col))
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    res += 1
        return res