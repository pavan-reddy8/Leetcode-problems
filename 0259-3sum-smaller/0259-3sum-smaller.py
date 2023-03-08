class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        res = [0]
        def twosum(t,l,r):
            while l < r:
                if nums[l]+nums[r]+t >= target:
                    r-=1
                else:
                    res[0]+=r-l
                    l+=1
                
        for i in range(len(nums)):
            twosum(nums[i],i+1,len(nums)-1)
        return res[0]