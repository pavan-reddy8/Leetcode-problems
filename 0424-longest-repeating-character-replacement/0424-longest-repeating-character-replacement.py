class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        d = [0] * 26
        res =0 

        while r < len(s):

            d[ord(s[r]) - ord('A')] +=1
            # print(l,r,r-l+1,max(d))
            # print(l,r,d)
            while r-l+1-max(d) > k:
                d[ord(s[l]) - ord('A')] -=1
                l+=1
            res = max(res,r-l+1)
            r+=1
                
        return res
            
                
        