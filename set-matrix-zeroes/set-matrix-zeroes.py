class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C= len(matrix[0])
        rflag=False
        cflag=False
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    if i == 0 :
                        rflag=True
                    if j == 0:
                        cflag=True
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1,R):
            for j in range(1,C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j]=0
                    
        if rflag == True:
            for j in range(C):
                matrix[0][j] = 0
        if cflag == True:
            for i in range(R):
                matrix[i][0] = 0
        print(matrix)
                
        
                    