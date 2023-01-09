class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(mat):
            l,r = 0,len(mat)-1
            while l<=r:
                mid = (l+r)//2
                if mat[mid] == target:
                    return True
                elif mat[mid] > target:
                    r = mid -1
                else:
                    l = mid +1
            return False
        
        
        for mat in matrix:
            l = len(mat)-1
            if mat[0] <= target and mat[l] >= target:
                if search(mat):
                    return True
        return False