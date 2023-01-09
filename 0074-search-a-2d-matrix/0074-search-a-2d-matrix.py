class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(p,l,r):
            while l<=r:
                mid = (l+r)//2
                if matrix[p][mid] == target:
                    return True
                elif matrix[p][mid] > target:
                    r = mid -1
                else:
                    l = mid +1
            return False
        
        u,d,l,r = 0,len(matrix)-1,0,len(matrix[0])-1
        
        while u <= d:
            p = (u+d)//2
            
            if matrix[p][0] == target:
                return True
            elif matrix[p][0] > target:
                d = p -1
            else:
                u = p +1
            
            if search(p,l,r):
                return True
        return False