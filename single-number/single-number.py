class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        min = 999
        for num in nums:
            if num in d:
                d[num] = d[num]+1
            else:
                d[num] = 1
        for k in d:
            if min > d[k]:
                min = d[k]
                inx = k
        return inx
        