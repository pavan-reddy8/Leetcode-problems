class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        com = []
        nums.sort()
        def backtrack(s,p):
            if s > target:
                return
            if s == target and com not in res:
                res.append(com.copy())
                return
            for i in range(p,len(nums)):
                if i == p:
                    com.append(nums[i])
                    backtrack(s+nums[i],i+1)
                    com.pop()
                elif nums[i-1] != nums[i]:
                    com.append(nums[i])
                    backtrack(s+nums[i],i+1)
                    com.pop()
                    
                
        backtrack(0,0)
        return res
        