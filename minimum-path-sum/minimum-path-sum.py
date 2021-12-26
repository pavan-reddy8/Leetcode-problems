class Solution:
    def minPathSum(self, g: List[List[int]]) -> int:
        for i in range(len(g)):
            for j in range(len(g[0])):
                if i==0 and j==0:
                    continue
                if i==0:
                    g[i][j] = g[i][j] + g[i][j-1]  
                elif j ==0:
                    g[i][j] = g[i][j] + g[i-1][j]
                else:
                    g[i][j] = min(g[i][j] + g[i-1][j] ,g[i][j] + g[i][j-1])
        print(g)
        return g[i][j]
                    
                    