class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for task in tasks:
            d[task] +=1
        
        counts = list(d.values())
        for i in range(len(counts)):
            counts[i] = -counts[i]
        
        
        heapq.heapify(counts)
        print(counts)
        q = []
        time = 0
        while counts or q:
            # print(counts,time)
            time+=1
            if counts:
                count = 1 + heapq.heappop(counts)
                if count:
                    q.append([count,time+n])
                # print(q)
            if q and q[0][1] == time:
                heapq.heappush(counts,q[0][0])
                q.pop(0)
         
 
        return time
        
            
        