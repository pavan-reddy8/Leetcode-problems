class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h) -1
        maxarea = 0
        area = 0
        while l < r:
            
            area = (r-l) * min(h[l],h[r])
            maxarea = area if maxarea < area else maxarea
            if h[l] < h[r]:
                l+=1
            elif h[l] > h[r]:
                r-=1
            else:
                if h[l+1] > h[r-1]:
                    l+=1
                else:
                    r-=1
            
        return maxarea