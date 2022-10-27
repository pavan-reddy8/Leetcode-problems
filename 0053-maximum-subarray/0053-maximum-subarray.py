class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subSum = nums[0]
        curSum = 0
        
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            subSum = max(subSum,curSum) 
        return subSum