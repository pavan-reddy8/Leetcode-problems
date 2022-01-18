class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res =[]
        for v in nums:
            nums[abs(v)-1]*=-1
            if nums[abs(v)-1] > 0:
                res.append(abs(v))
        return res
        