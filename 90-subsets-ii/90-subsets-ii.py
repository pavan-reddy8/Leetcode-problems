class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        nums.sort()
        for v in nums:
            n = len(res)
            j = 0
            while j<n:
                l = res[j].copy()
                l.append(v)
                if l not in res:
                    res.append(l)
                j += 1
        return res
                
                
        