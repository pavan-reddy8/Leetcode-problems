class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         d={}
#         inx = 0
#         m = 1
#         count = 0
#         for num in nums:
#             d[num] = 1
#         for num in nums:
#             d[num]+=1
#             inx,m = (num,d[num]) if d[num] > m else (inx,m)
            
            
#         return inx
    
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        n = 0
        for num in nums:
            if n == num:
                count += 1
            else:
                if count <= 0:
                    n = num
                    count = 1
                else:
                    count -= 1

            
            
        return n
        
    