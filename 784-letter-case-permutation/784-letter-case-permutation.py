class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res =[]
        res.append(s)
        for i in range(len(s)):
            if not s[i].isnumeric():
                n = len(res)
                while n != 0:
                    s1 = res.pop(0)
                    sl = s1[0:i]
                    sr = s1[i+1:len(s)]
                    res.append(sl+s[i].lower()+sr)
                    res.append(sl+s[i].upper()+sr)
                    n-=1
        return res
            