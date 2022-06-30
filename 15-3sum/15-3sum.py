class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            if i != 0 and nums[i-1] == nums[i]:
                i +=1
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l +=1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    li = []
                    li.extend((nums[i],nums[l],nums[r]))
                    l +=1 
                    r -= 1
                    if li not in res and len(li) != 0: 
                        res.append(li)
                        
            i += 1
        return res
                    
                
            
                
    