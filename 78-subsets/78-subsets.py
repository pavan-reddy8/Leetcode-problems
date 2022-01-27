class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        res.append([nums[0]])
        
        for i in range(1,len(nums)):
            n = len(res)
            j = 0
            while j < n:
              
                l = res[j].copy()
                l.append(nums[i])
                res.append(l)
                j +=1
        return res
            
        