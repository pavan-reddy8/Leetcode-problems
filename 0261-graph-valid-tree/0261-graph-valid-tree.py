class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = defaultdict(list)
        for (v1,v2) in edges:
            d[v1].append(v2)
            d[v2].append(v1)
        
        visited = set()
        cycle = set()
        # print(d)
        def dfs(v,pv):
            # print(cycle)
            if v in cycle:
                return False
            visited.add(v)
            cycle.add(v)
            res = True
            for vi in d[v]:
                if vi != pv:
                    res &= dfs(vi,v)
            return res
        
        
        res = dfs(0,-1)
        if len(cycle) != n:
            return False
        return res
                
        