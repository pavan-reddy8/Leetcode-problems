class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"}
        res = []
        ans = [""]
        def dfs(i):
            if i == len(digits):
                res.append(ans[0][:])
                return
            if i > len(digits):
                return
            for l in d[digits[i]]:
                ans[0] += l
                dfs(i+1)
                ans[0] = ans[0][:-1]
        if digits == "" :
            return []
        dfs(0)
        return res
                
                
        