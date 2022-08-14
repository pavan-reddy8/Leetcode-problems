class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {}
        for pre in prerequisites:
            if pre[1] not in d:
                d[pre[1]] =[pre[0]]
            else:
                d[pre[1]].append(pre[0])
       
        res = [True]
        visited = set()
        def dfs(pre):
            visited.add(pre)
            if pre not in d or d[pre] == []:
                return
            for prei in d[pre]:
                if prei in visited:
                    res[0] = False
                    return
                dfs(prei)
                visited.remove(prei)
            d[pre] = []
        for i in range(numCourses):
            dfs(i)
            visited.remove(i)
        return res[0]