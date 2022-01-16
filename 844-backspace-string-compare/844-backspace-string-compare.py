class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sl = list(s)
        tl = list(t)
        def clean(sl):
            si=0
            res =[]
            while si < len(sl): 
                if res and sl[si] == '#':
                    res.pop()
                elif sl[si] != '#':
                    res.append(sl[si])
                si += 1
            return res
        sl = clean(sl)
        tl = clean(tl)
        return sl == tl