class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        si = set()
        substr = 0
        while r < len(s):
            substr = max(substr,r - l)
            if s[r] not in si:
                si.add(s[r])
                substr = max(substr,r - l +1)
                r+=1
                
            else:
                while s[l] != s[r]:
                    si.remove(s[l])
                    l+=1
                si.remove(s[l])
                si.add(s[r])
                l+=1
                r+=1
        return substr
        