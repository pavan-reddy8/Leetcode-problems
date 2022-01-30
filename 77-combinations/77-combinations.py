class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        per =[]
        def backtrack(start):
            if len(per) == k:
                if per not in res:
                    res.append(per.copy())
                return
            while start < n+1:
                    per.append(start)
                    backtrack(start+1)
                    per.pop()
                    start+=1
        backtrack(1)
        return res