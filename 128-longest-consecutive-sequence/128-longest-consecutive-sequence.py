class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset=set(nums)
        res = 0
        for v in nums:
            count =1
            if v-1 not in numsset:
                count = 1
                while v+count in numsset:
                    count+=1
            res = max(res,count)
        return res