class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(index,result):
            if index == len(nums):
                if result == target:
                    return 1
                else:
                    return 0
            if (index,result) in dp:
                return dp[(index,result)]
            
            dp[(index,result)] = dfs(index+1,result-nums[index])+ dfs(index+1,result+nums[index])
            return dp[(index,result)]
        
        return dfs(0,0)
            
        