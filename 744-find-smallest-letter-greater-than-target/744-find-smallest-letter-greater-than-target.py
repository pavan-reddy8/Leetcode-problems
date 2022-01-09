class Solution:
    def nextGreatestLetter(self, s: List[str], t: str) -> str:
        diff = ord(s[0])
        for c in s:
            if ord(c)-ord(t) > 0:
                diff = min(ord(c)-ord(t),diff)
        
        res = chr(diff) if diff == ord(s[0])  else chr(ord(t) + diff) 
        return res