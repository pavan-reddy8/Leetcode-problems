class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def twosum(target,l,r):
            while l < r:
                if nums[l]+nums[r] == -target:
                    if [target,nums[l],nums[r]] not in res:
                        res.append([target,nums[l],nums[r]])
                    l+=1
                    r-=1
                elif nums[l]+nums[r] > -target:
                    r-=1
                else:
                    l+=1
                
        for i in range(len(nums)):
            if i == 0:
                twosum(nums[i],i+1,len(nums)-1)
                a = nums[i]
            else:
                if a != nums[i]:
                    twosum(nums[i],i+1,len(nums)-1)
                    a = nums[i]
        return res
            
        