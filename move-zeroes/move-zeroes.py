class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos0 = 0 
        for i,val in enumerate(nums):
            if nums[i] != 0:
                nums[pos0],nums[i] = nums[i],nums[pos0]
                pos0 += 1

                