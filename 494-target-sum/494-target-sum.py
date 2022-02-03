class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        d={}
        def backtrack(i,sum):
            if i == len(nums):
                return 1 if sum == target else 0
            if (i,sum) in d :   
                return d[(i,sum)]
            d[(i,sum)] = backtrack(i+1,sum+nums[i])+backtrack(i+1,sum-nums[i])
            return d[(i,sum)]  
        return backtrack(0,0)

            