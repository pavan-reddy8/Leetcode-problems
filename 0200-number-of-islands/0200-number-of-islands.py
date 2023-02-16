class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        def dfs(r,c,visited):
            if (r,c) in visited or r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == "0":
                return
            # print(visited)
            visited.add((r,c))
            for (a,b) in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(r+a,c+b,visited)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] != "0":
                    count+=1
                    dfs(r,c,visited)
        return count
            