class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        
        visited = set()
        res = True
        d = defaultdict(list)
        for (s1,s2) in pre:
            d[s2].append(s1)
            
        def dfs(s):
            if not d[s]:
                return True
            if s in visited:
                return False
            visited.add(s)
            for si in d[s]:
                if not dfs(si):
                    return False
            visited.remove(s)
            d[s] = []
            return True
        
        for (s1,s2) in pre:
                res &= dfs(s2)
        return res
            
        