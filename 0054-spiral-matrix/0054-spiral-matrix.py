class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        t, l, b, r = 0, 0, len(matrix)-1, len(matrix[0])-1
        i = l
        while l <= r and t <= b:
            while i <= r:
                res.append(matrix[t][i])
                i+=1
            t +=1
            i = t
            
            while i <= b:
                res.append(matrix[i][r])
                i+=1
            r -= 1
            i = r
            if l <=r and t<=b:
                while i >= l:
                    res.append(matrix[b][i])
                    i-=1
                b -= 1
                i = b

                while i >= t:
                    res.append(matrix[i][l])
                    i-=1
                l +=1
                i = l
            
        return res