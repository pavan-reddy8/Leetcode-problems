class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d ={}
        for v in nums:
            if d.get(v):
                return v
            else:
                d[v]=1
                
        