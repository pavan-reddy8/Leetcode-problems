class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        per=[]
        res=[]
        used=[False]*len(nums)
        def backtrack():
            if len(per) == len(nums):
                if per not in res:
                    res.append(per.copy())
                return
            for i,v in enumerate(nums):
                if not used[i]:
                    used[i]=True
                    per.append(v)
                    backtrack()
                    used[i]=False
                    per.pop()
        backtrack()
        return res