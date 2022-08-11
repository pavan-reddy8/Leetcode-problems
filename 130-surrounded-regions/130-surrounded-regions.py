class Solution:
    def solve(self, b: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        
        def dfs(r, c):
            if b[r][c] == "X":
                return
            b[r][c] ="T"
            moves = [(0,1),(0,-1),(1,0),(-1,0)]
            for cr, cc in moves:
                row = r+cr
                col = c+cc
                if 0 <= row< len(b) and 0<= col <len(b[0]) and b[row][col] !="T":
                    dfs(row,col)
                

        
        for r in range(len(b)):
            for c in range(len(b[0])):
                if (r in [0,len(b)-1] or c in [0,len(b[0])-1]) and b[r][c] == "O":
                    dfs(r,c)
        
        for r in range(len(b)):
            for c in range(len(b[0])):
                if b[r][c] == "O":
                    b[r][c] = "X"
                elif b[r][c] == "T":
                    b[r][c] = 'O'