class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        per=[]
        res=[]
        used=[False]*len(nums)
        def backtrack():
            if len(per) == len(nums):
                print(per)
                res.append(per.copy())
                return
            for i,v in enumerate(nums):
                if not used[i]:
                    used[i]=True
                    per.append(v)
                    backtrack()
                    used[i]=False
                    per.remove(v)
        backtrack()
        return res
                