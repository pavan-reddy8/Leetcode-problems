class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r = len(nums)-1
        l = 0
        while r >=0 and nums[r] >= 0:
            r -=1
        neg = nums[:r+1]
        neg.reverse()
        pos = nums[r+1:]
        print(neg,pos)
        l,r=0,0
        for i in range(len(nums)):
            if l< len(neg) and r<len(pos):
                if abs(neg[l]) < abs(pos[r]):
                    nums[i] = neg[l] **2
                    l+=1
                else:
                    nums[i] = pos[r] **2
                    r+=1
            else:
                nums[i],l,r = (neg[l] **2,l+1,r) if l< len(neg) else  (pos[r] **2,l,r+1)
                
        return nums
        
        
        