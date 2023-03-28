class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        count = [[] for i in range(len(nums)+1)] 
        res =[]
        # print(count)
        for i in nums:
            d[i] += 1
        
        for i in d:
            if d[i] != 0:
                count[d[i]].append(i)
        
#         print(d)
#         print(count)
        for li in range(len(count)-1,0,-1):
            if len(count[li]) != 0:
                for i in count[li]:
                    res.append(i)
                    k -= 1
            if k == 0:
                break
        return res
        
            