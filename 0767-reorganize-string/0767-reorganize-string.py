class Solution:
    def reorganizeString(self, s: str) -> str:
        d = defaultdict(int)
        for si in s:
            d[si] += 1
        print(d)
        heap = []
        q =[]
        res = ''
        for di in d:
            heap.append([-d[di],di])
        print(heap)
        heapq.heapify(heap)
        prev = None
        
        while heap or prev:
            print(heap,prev)
            if prev and not heap:
                print(res)
                return ''
            cur = heapq.heappop(heap)
            print(cur)
            cur[0] += 1
            res += cur[1]
            
            if prev:
                    heapq.heappush(heap,prev)
                    prev = None
            if cur[0]:
                prev = cur.copy()
                
        
        return res
            
        
            