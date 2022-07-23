class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointDis=[]
        res =[]
        for point in points:
            pointDis.append([ point[0]**2 + point[1]**2 ,point[0],point[1] ])
        heapq.heapify(pointDis)
        
        while k>0:
            dis, x, y = pointDis[0]
            res.append([x,y])
            heapq.heappop(pointDis)
            k-=1
        return res