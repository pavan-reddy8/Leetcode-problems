class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(m)):
            for j in range(i,len(m[0])):
                m[i][j],m[j][i]=m[j][i],m[i][j]
            m[i].reverse()