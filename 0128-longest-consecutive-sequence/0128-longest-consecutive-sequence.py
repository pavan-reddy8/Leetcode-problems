class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        long = 0
        sublong =0
        for i in nums:
            if i-1 in s:
                continue
            else:
                j = i
                while (j) in s:
                    sublong += 1
                    j+=1
                long = sublong if sublong > long else long
                sublong = 0
        return long