class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = len(nums)
        totalsum = ((m+1) * m)//2
        for num in nums:
            print(totalsum)
            totalsum -= num
        return totalsum