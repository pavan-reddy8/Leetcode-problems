class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        count = [-1]
        q = []
        
        def bfs(q,visited):
            while q:
                lq = len(q)
                while lq:
                    r,c = q.pop(0)
                    moves = [(0,1),(0,-1),(1,0),(-1,0)]
                    for move in moves:
                        row = r+move[0]
                        col = c+move[1]
                        if 0<=row<len(grid) and 0<=col<len(grid[0]) and (row,col) not in visited and grid[row][col] == 1:
                            visited.add((row,col))
                            q.append((row,col))
                            grid[row][col] = 2
                    lq -=1
                count[0]+=1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))

        bfs(q,visited)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        if not visited:
            return 0
        return count[0]
                    
                            
        