class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        global f 
        f = 0
        for li in grid:
            l = 0
            mid =0
            r= len(li)-1
            while l < r:
                mid = l+(r-l)//2
                if li[mid]<0:
                    f = 1
                    r = mid
                else:
                    l = mid+1
             
            if li[r]<0:count += len(li)-r

                
        return count  
                
                
                