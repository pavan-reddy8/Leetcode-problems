class Solution:
    def countSubstrings(self, s: str) -> int:
        l = r = m = 0
        o = 0
        while m < len(s):
            if l < 0 or r > len(s)-1:
                m += 1
                l = r = m
            else:
                if s[l] == s[r]:
                    o += 1
                    l -=1
                    r +=1
                else:
                    m += 1
                    l = r = m
        l = m = 0
        m = r = 1
        e = 0
        while m < len(s):
            if l < 0 or r > len(s)-1:
                m += 1
                l = m - 1
                r = m
                
            else:
                if s[l] == s[r]:
                    e += 1
                    l -=1
                    r +=1
                else:
                    m += 1
                    l = m -1
                    r = m
                    
        print(o,e)        
        return e+o