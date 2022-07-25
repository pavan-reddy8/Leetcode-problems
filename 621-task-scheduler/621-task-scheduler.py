class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        heap =[]
        q = []
        for task in tasks:
            if task not in d:
                d[task] = 1
            else:
                d[task] += 1
        for item in d:
            heap.append([-d[item],item])
        heapq.heapify(heap)
        time = 0
        while heap or q:

            if heap:
                cur = heap[0]
                heapq.heappop(heap)
                if cur[0]+1 !=0:
                    q.append([time+n,cur[0]+1,cur[1]])
            if q and q[0][0] == time:
                time, freq, char= q.pop(0)
                heapq.heappush(heap,[freq,char])    
            
            time+=1
            # print("time" ,time)
            # print("heap",heap)
            # print("q",q)
            # print("------------")
        return time
            
        
        
        