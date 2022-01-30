class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        com =[]
        def backtrack(s,st):
            if target < s:
                return
            if target == s:
                res.append(com.copy())
                return
            for i in range(st,len(nums)):
                com.append(nums[i])
                backtrack(s+nums[i],i)
                com.pop()
        backtrack(0,0)
        return res