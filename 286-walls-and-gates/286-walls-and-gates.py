class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visited = set()
        def bfs (q):
            dist = 0
            while q:
      
                r,c = q.pop(0)
                moves = [(0,1),(0,-1),(1,0),(-1,0)]
                for move in moves:
                    row = r + move[0]
                    col = c + move[1]
                    if 0 <= row < len(rooms) and 0 <= col < len(rooms[0]) and (row,col) not in visited and rooms[row][col] != -1 and rooms[row][col] != 0:
                        dist = min(dist,rooms[r][c])
                        dist+=1
                        rooms[row][col] = dist
                        visited.add((row,col))
                        q.append((row,col))

        q = []
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    q.append((r,c))
        bfs(q)
                    
                    
                    
        
        