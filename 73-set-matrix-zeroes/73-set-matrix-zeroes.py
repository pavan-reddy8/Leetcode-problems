class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        c=[0]*m
        r=[0]*n
        print(c,r)
        for i in range(n):
            for j in range(m):
                r[i] = (r[i]+1) if matrix[i][j] == 0 else r[i]
        for i in range(m):
            for j in range(n):
                c[i] = (c[i]+1) if matrix[j][i] == 0 else c[i]
        print(c,r)
        for i in range(n):
                if r[i] > 0:
                    matrix[i] = [0]*m
        for i in range(m):
            for j in range(n):
                if c[i] > 0:
                    matrix[j][i] = 0