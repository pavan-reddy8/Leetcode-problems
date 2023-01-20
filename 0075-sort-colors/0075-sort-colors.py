class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0,len(nums)-1
        i=0
        
        while i <= r: 
            # print(nums,i,r)
            if nums[i] == 0:
                nums[l],nums[i] = nums[i],nums[l]
                l+=1
            elif nums[i] == 2:
                nums[r],nums[i] = nums[i],nums[r]
                i-=1
                r-=1
            i+=1

        