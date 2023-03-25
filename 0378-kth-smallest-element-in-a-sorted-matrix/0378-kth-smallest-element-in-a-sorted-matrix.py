class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        for li in matrix:
            for i in li:
                l.append(i)
            
        heapq.heapify(l)
        
        for i in range(k):
            res = heapq.heappop(l)
            
        return res
        