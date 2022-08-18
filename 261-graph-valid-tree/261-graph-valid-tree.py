class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = defaultdict(list)
        for v1,v2 in edges:
            d[v1].append(v2)
            d[v2].append(v1)
        visited = set()
        cycle = set()
        
        def dfs(v,pv):
            print(v,d[v])
            if v in cycle:
                return False
            cycle.add(v)
            for vi in d[v]:
                print(v,vi)
                if vi == pv:
                    continue
                if not dfs(vi,v):
                    return False
            return True
        
        res = dfs(0,None)
        if len(cycle) == n:
            return res
        return False
        