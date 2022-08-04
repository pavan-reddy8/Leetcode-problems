class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(s):
            l = 0
            r = len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        res = []
        subset = []
        sub = ""
        def backtrack(i,sub):
            if i >= len(s):
                res.append(subset.copy())
                return
            for j in range(i,len(s)):
                sub = s[i:j+1]
                if ispalindrome(sub):
                    subset.append(sub[:])
                    backtrack(j+1,sub)
                    subset.pop()
        backtrack(0,sub)
        return res
            
            
                    