class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        as1 = [0] *26
        n = len (s1)
        as2 = [0] *26
        for c in s1:
            as1[ord(c)-ord('a')]+=1
        for i in range(len(s2)):
            if i < n:
                as2[ord(s2[i])-ord('a')] += 1
            else:
                as2[ord(s2[i])-ord('a')] += 1
                as2[ord(s2[i-n])-ord('a')] -= 1
            if as1 == as2:
                return True
        
#         l,r = 0,0
#         while r < len(s2):
#             as2[ord(s2[r])-ord('a')]+=1

#             if r-l+1 == n:
#                 print(as2)
#                #print(as1)
#                 l = r+1
#                 if as1 == as2:
#                     return True
#                 as2 = [0] *26
#             r += 1

            
                    
 
        
        return False