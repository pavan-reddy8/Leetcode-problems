class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        xmin = points[0][0]
        xmax = points[0][1]
        res = 1
        for [curmin,curmax] in points[1:]:
            if curmin > xmax:
                res += 1
                xmax = curmax
            else:
                xmax = min(xmax,curmax)
                
        print(res)
        print(points)
        return res
        