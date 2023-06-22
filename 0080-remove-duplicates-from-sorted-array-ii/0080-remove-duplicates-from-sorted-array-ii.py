class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        l,r = 1,1
        if len(nums) == 1:
            return 1 
        while r < len(nums):
            if nums[r] == nums[r-1]:
                count +=1
            else:
                count = 1
            if count <=2:
                nums[l] = nums[r]
                l+=1
            r+=1
        print(l)
        return l


            
            
        