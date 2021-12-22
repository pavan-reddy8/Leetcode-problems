class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        di = {}
        res = []
        for v in n:
            if (di.get(v) is None):
                di[v] = 1
            else: di[v] += 1
        di = sorted(di.items(), key=lambda x:x[1] ,reverse = True)
        # print(di)
        for i,v in di:
            if k!=0 :
                res.append(i)
                k -= 1
            else:
                break
        return res