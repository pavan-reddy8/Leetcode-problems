class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkthepiles(speed):
            time = 0
            for i in piles:
                time += ceil(i/speed)
            return time
        
        l = 1
        r = max(piles) 
        res = r
        while l <= r:
            
            p = (l+r)//2
         
            eta = checkthepiles(p)
            
            if eta <= h:
                res = min(res,p)
                r = p-1
            else:
                l = p+1
        return res
        
                