class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res =[[1]* (n)] * (m)
        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = res[i][j-1] + res[i-1][j] 
        return res[m-1][n-1]

        