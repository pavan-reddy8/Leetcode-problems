class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        heap = []
        for c in s:
            d[c] += 1
        for i in d:
            heap.append([-d[i],i])
        heapq.heapify(heap)
        res = ''
        while heap:
            prev = heapq.heappop(heap)
            while prev[0] != 0:
                prev[0]+=1
                res += prev[1]
                
        return res
            
            
        