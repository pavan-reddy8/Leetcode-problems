class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        d ={}
        l = [0] * 26 
        for v in s:
            for i in v:

                if l[ord(i)-ord('a')] == 0:
                    l[ord(i)-ord('a')] = 1
                else:
                    l[ord(i)-ord('a')] += 1
            t = tuple(l)
            l = [0] * 26
            if d.get(t) is None:
                a =[]
                a.append(v)
                d[t]=a
            else:
                d[t].append(v) 
        return d.values()
                
                
        