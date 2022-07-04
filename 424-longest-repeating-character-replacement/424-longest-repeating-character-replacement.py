class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # l = 0
        # newl = 1
        # r = 1
        # count = 1
        # ki =k
        # while r < len(s):
        #     if s[l] == s[r]:
        #         count = max(count,r-l+1)
        #         r += 1
        #     elif s[l] != s[r] and ki > 0:
        #         count = max(count,r-l+1)
        #         newl = r
        #         r += 1
        #         ki -= 1
        #     else:
        #         ki = k
        #         l = newl
        #         r = newl +1
        #         newl = r
        # return count
        d = {}
        for c in s:
            d[c] = 0
        l = 0
        count =0
        for r in range(len(s)):
            d[s[r]] += 1
            while (r-l+1) - max(d.values()) > k:
                d[s[l]]-=1
                l+=1
            count = max(r-l+1,count)
            
            
            
        return count
                
                