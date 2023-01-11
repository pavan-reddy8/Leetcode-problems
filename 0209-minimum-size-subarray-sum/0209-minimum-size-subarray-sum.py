class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        l,r = 0,0
        total = 0
        while r < len(nums):
            total += nums[r]
            while total >= target:
                total -= nums[l]
                res = min(res,r-l+1)
                l+=1
            r+=1
        if res == len(nums) +1:
            return 0
        return res