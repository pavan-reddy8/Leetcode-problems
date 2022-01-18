class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res =[]
        for v in nums:
            i =abs(v)-1
            nums[i]*=-1
    
            if nums[i] > 0:
                res.append(abs(v))
        return res
        