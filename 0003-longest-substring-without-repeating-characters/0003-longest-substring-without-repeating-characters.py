class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()
        l,r = 0,0
        res = 0
        while r < len(s):
            while s[r] in d:
                d.remove(s[l])
                l+=1
            d.add(s[r])
            res = max(r-l+1,res)
            r+=1
        return res
                
            
        