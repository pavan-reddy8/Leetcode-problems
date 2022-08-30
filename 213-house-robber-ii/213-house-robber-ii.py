class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        dp = [0]*(len(nums)-1)
        dp[0] = nums[0]
        dp[1] = max(dp[0],nums[1])
        for i in range(2,len(nums)-1):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        dp1 = [0]*len(nums)
        dp1[1] = nums[1]
        dp1[2] = max(dp1[1],nums[2])
        for i in range(3,len(nums)):
            dp1[i] = max(nums[i]+dp1[i-2],dp1[i-1])
        return max(dp[-1],dp1[-1])
        
        