class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        per =[]
        def backtrack(start):
            if len(per) == k:
                if per not in res:
                    res.append(per.copy())
                return
            for i in range(start,n+1):
                    per.append(i)
                    backtrack(i+1)
                    per.pop()
        backtrack(1)
        return res