class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            temp = nums[abs(num)-1]
            if temp < 0:
                return abs(num)
            nums[abs(num)-1] = -nums[abs(num)-1]
            