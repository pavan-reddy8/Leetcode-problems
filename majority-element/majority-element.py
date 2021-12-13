class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        inx = 0
        m = 1
        for num in nums:
            d[num] = 1
        for num in nums:
            d[num]+=1
            inx = num if d[num] > m else inx
            m=max(m,d[num])
            
        return inx
        