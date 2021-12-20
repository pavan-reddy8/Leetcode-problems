class Solution:
    def maxProfit(self, p: List[int]) -> int:
        
        
#         r = len(p)-1
#         l = 0
#         max_p = 0
#         while l<=r:
#             if p[l] >= p[r] and l is not r:
#                 r-=1
#             elif p[l] < p[r] :
#                 max_p = (p[r]-p[l]) if max_p < (p[r]-p[l]) else max_p
#                 r-=1
#             else:
#                 l+=1
#                 r=len(p)-1
#         return max_P
            min_pr = p[0] 
            max_p = 0
            for pr in p:
                min_pr = min(pr,min_pr)
                p = pr - min_pr
                max_p = max(p,max_p)

            return max_p